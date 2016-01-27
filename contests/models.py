from django.db import models
from django.utils import timezone




class Contest(models.Model):
    start_date = models.DateTimeField(default=timezone.now())
    name = models.CharField(max_length=50, unique=True)




