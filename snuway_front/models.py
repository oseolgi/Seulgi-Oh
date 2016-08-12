from django.db import models


from django.conf import settings

# Create your models here.

class Date(models.Model):
    title = models.CharField(max_length=10)
    start = models.DateTimeField()
    end = models.DateTimeField()
    description = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.title