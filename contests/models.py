from django.db import models

class Contests(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    name = models.CharField(max_length=50)
