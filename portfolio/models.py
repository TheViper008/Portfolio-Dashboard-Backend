from django.db import models

# Create your models here.

class Holding(models.Model):
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    avg_price = models.FloatField()
    current_price = models.FloatField()
    sector = models.CharField(max_length=50)
    market_cap = models.CharField(max_length=10)