from django.db import models
from django.contrib.postgres.fields import JSONField


class Rider(models.Model):
    id = models.AutoField(primary_key=True)
    rider_id = models.CharField(max_length=50, unique=True, db_index=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50)
    dob = models.DateTimeField()
    sex = models.CharField(max_length=6)
    contact_number = models.CharField(max_length=15, db_index=True)
    contact_email = models.CharField(max_length=50)
    blood_group = models.CharField(max_length=20)
    emergency_name = models.CharField(max_length=50)
    emergency_number = models.CharField(max_length=15)
    area = models.CharField(max_length=50)
    address = models.TextField(null=True)
    max_distance = models.IntegerField()
    chapter = JSONField(default=None)
    bicycle = JSONField(default=None)
    AOI = JSONField(default=None)
    terrain = JSONField(default=None)
    goals = models.TextField()
    expectations = models.TextField()
    event_types = models.TextField()
    comments = models.TextField()

    class Meta:
        db_table = 'riders'
