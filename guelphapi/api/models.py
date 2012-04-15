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

# Incredibly unpredictable data
# shove it all into a textfield
class Event(models.Model):
    title = models.TextField()
    organization = models.TextField()
    description = models.TextField()
    eligibility = models.TextField()
    event_format = models.TextField()
    instructors = models.TextField()
    topic = models.TextField()
    contact = models.TextField()
    location = models.TextField()
    maximum_attendance = models.TextField()
    time = models.TextField()
    date = models.TextField()
    qualifies_as = models.TextField()
    more_information = models.TextField()
    advanced_registration = models.TextField()
    link = models.URLField()

    def __unicode__(self):
        return "%s - %s %s" % (self.title, self.date, self.time)
