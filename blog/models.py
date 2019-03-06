from django.conf import settings
from django.db import models
from django.utils import timezone


class PostModel(models.Model):

    tablename = models.CharField(max_length=200)
    providername = models.CharField(max_length=200)
    filter = models.CharField(max_length=200)
    join = models.CharField(max_length=200)
    sortfield = models.CharField(max_length=200)
    usecase = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.tablename

    def __str__(self):
        return self.providername
