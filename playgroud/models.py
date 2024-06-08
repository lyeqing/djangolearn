from django.db import models

import uuid

class Persons(models.Model):
    person_id = models.AutoField(primary_key=True)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    address = models.CharField(max_length=255, null=True, blank=True)
    suburb = models.CharField(max_length=100, null=True, blank=True)
    postcode = models.CharField(max_length=10, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    password = models.CharField(max_length=128)
    token = models.UUIDField(default=uuid.uuid4, null=True, blank=True)


class Activities(models.Model):
    activity_id = models.AutoField(primary_key=True)
    person = models.ForeignKey('Persons', on_delete=models.CASCADE, null=False, blank=False)
    category = models.CharField(max_length=100, null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    log_time = models.DateTimeField()