from urllib import response
from django.db import models

class MockData(models.Model):
    status = models.CharField(max_length=10)
    message = models.CharField(max_length=255)
    data = models.JSONField(null=True, blank=True, verbose_name='Response data property')
    request_data = models.JSONField(null=True, blank=True)
