from django.contrib.auth.models import User
from django.db import models

from tastypie.models import create_api_key

# Auto generate API key for each user
models.signals.post_save.connect(create_api_key, sender=User)

class News(models.Model):
    title = models.TextField()
    datetime_published = models.DateTimeField()
    link = models.URLField()
    content = models.TextField()
    category = models.TextField()

    class Meta:
        verbose_name_plural = "news"

    def __unicode__(self):
        return "%s (%s)" % (self.title, self.datetime_published)

# We use all TextFields here, because the data coming in is
# very unpredictable, and in PostgreSQL, there is no performance difference
# http://www.postgresql.org/docs/9.1/static/datatype-character.html
class Course(models.Model):
    code = models.TextField()
    number = models.TextField()
    department = models.TextField()
    title = models.TextField()
    semesters = models.TextField()
    credit = models.TextField()
    description = models.TextField()
    restrictions = models.TextField()
    prerequisites = models.TextField()

    def __unicode__(self):
        return "%s - %s" % (self.code, self.title)
