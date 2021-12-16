from django.db import models


class NewsSource(models.Model):
    id = models.CharField(primary_key=True, max_length=50, null=False, blank=False)
    name = models.CharField(unique=True, max_length=50, null=False, blank=False)
    language = models.CharField(max_length=2, null=False, blank=False)
    country = models.CharField(max_length=2, null=False, blank=False)
