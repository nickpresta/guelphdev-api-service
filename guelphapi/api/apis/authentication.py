import base64
import ldap

from django.contrib.auth.models import User

from tastypie.authentication import BasicAuthentication
from tastypie.http import HttpUnauthorized
from tastypie.models import ApiKey

class BasicHttpApiKeyAuthentication(BasicAuthentication):
    """This is a mashup of Basic HTTP Auth, and ApiKey authentication.

    Its purpose to is to check two things:

    1. As a developer, that you have a valid API key in request.GET.
    2. As a client, that you have valid uog credentials (basic HTTP Auth).

    If you don't have a valid api key, you can't use our API.
    If you don't have valid uog credentials, you can't get your data.
    """

    def extract_credentials(self, request):
        username = request.GET.get('username')
        api_key = request.GET.get('api_key')

        return username, api_key

    def get_key(self, user, api_key):
        try:
            ApiKey.objects.get(user=user, key=api_key)
        except ApiKey.DoesNotExist:
            return False

        return True

    def is_authenticated(self, request, **kwargs):
        # Do API check, as that is a local check, should be faster
        try:
            username, api_key = self.extract_credentials(request)
        except ValueError:
            return HttpUnauthorized()

        if not username or not api_key:
            return HttpUnauthorized()

        try:
            user = User.objects.get(username=username)
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return HttpUnauthorized()

        if not self.get_key(user, api_key):
            return HttpUnauthorized()

        # Do our Http Basic Auth check now
        # Check with remote LDAP server, too

        if not request.META.get('HTTP_AUTHORIZATION'):
            return self._unauthorized()

        try:
            auth_type, data = request.META.get('HTTP_AUTHORIZATION', '').split()
        except ValueError:
            return self._unauthorized()

        if auth_type.lower() != 'basic':
            return self._unauthorized()

        user_pass = base64.b64decode(data)
        bits = user_pass.split(':', 1)

        if len(bits) != 2:
            return self._unauthorized()

        # Check with LDAP
        try:
            ldap_server = ldap.initialize('ldaps://directory.uoguelph.ca')
            base_dn = 'uid=%s,ou=People,o=uoguelph.ca' % bits[0]
            ldap_server.simple_bind_s(base_dn, bits[1])
        except ldap.LDAPError, e:
            return self._unauthorized()

        request.user.username = bits[0]
        request.user.password = bits[1]

        return True


