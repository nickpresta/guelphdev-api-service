from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100)
    datetime_published = models.DateTimeField()
    link = models.URLField()
    content = models.TextField()
    category = models.CharField(max_length=100)

    def __unicode__(self):
        return "%s (%s)" % (self.title, self.datetime_published)

class Course(models.Model):
    code = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    department = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    semesters = models.CharField(max_length=50)
    credit = models.CharField(max_length=50)
    description = models.TextField()
    restrictions = models.CharField(max_length=100)
    prerequisites = models.CharField(max_length=100)

    def __unicode__(self):
        return "%s - %s" % (self.code, self.title)
