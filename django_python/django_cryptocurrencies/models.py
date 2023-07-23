from django.db import models

class Cryptocurrency(models.Model):
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    updated_at = models.DateTimeField(auto_now=True)