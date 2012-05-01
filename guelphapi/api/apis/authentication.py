import base64
import ldap
import logging

from django.conf import settings
from django.contrib.auth.models import User

from tastypie.authentication import BasicAuthentication
from tastypie.http import HttpUnauthorized
from tastypie.models import ApiKey

logger = logging.getLogger(__name__)
# Equivalent of "tls_checkpeer no"
# Since school uses self-signed cert
# We only use SSL as transport encryption anyways
ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_ALLOW)

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
            logger.info('Could not get username or API key from database.')
            return HttpUnauthorized()

        if not username or not api_key:
            logger.info('Username or API key are empty.')
            return HttpUnauthorized()

        try:
            user = User.objects.get(username=username)
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            logger.info('User does not exist/multiple users in database.')
            return HttpUnauthorized()

        if not self.get_key(user, api_key):
            logger.info('No valid API key for user %s.' % user)
            return HttpUnauthorized()

        # Do our Http Basic Auth check now
        # Check with remote LDAP server, too

        if not request.META.get('HTTP_AUTHORIZATION'):
            logger.info('No HTTP_AUTHORIZATION header in request.')
            return self._unauthorized()

        try:
            auth_type, data = request.META.get('HTTP_AUTHORIZATION', '').split()
        except ValueError:
            logger.info('Could not extract data from HTTP_AUTHORIZATION header.')
            return self._unauthorized()

        if auth_type.lower() != 'basic':
            logger.info('Authorization type not basic.')
            return self._unauthorized()

        user_pass = base64.b64decode(data)
        bits = user_pass.split(':', 1)

        if len(bits) != 2:
            logger.info('Length of bits != 2 in basic auth header.')
            return self._unauthorized()

        # Check with LDAP
        try:
            ldap_server = ldap.initialize(settings.LDAP_SERVER)
            base_dn = 'uid=%s,ou=People,o=uoguelph.ca' % bits[0]
            ldap_server.simple_bind_s(base_dn, bits[1])
        except ldap.LDAPError as e:
            logger.info('LDAP error: %s' % e)
            return self._unauthorized()

        request.user.username = bits[0]
        request.user.password = bits[1]

        return True

