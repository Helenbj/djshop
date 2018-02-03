from django.db import models
from datetime import date

# Create your models here.
class DiscountInfo(models.Model):
    title = models.CharField(max_length=500)
    lkurl = models.CharField(max_length=500)
    imgurl = models.CharField(max_length=500)
    merchant = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    date = models.DateField(default=date.today)
#    date = models.DateField(auto_now_add=True)
