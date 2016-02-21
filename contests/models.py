from django.db import models
from django.utils import timezone
from datetime import timedelta




class Contest(models.Model):
    start_date = models.DateTimeField('Start Date', null=True, blank=True)
    name = models.CharField(max_length=50, unique=True)

    def is_active(self):
        return self.expire_date <= self.start_date + timedelta(days=28)







