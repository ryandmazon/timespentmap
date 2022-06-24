from django.db import models


class TimeUsage(models.Model):
    uuid = models.UUIDField(primary_key=True, auto_created=True)
    country = models.CharField(null=False, max_length=255)
    category = models.CharField(null=False, max_length=255)
    time_mins = models.IntegerField(null=False)
