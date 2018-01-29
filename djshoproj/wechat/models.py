from django.db import models
from datetime import date

# Create your models here.
class DiscountInfo(models.Model):
    title = models.CharField(max_length=500)
    lkurl = models.CharField(max_length=500)
    imgurl = models.CharField(max_length=500)
    keywords = models.CharField(max_length=300)
    date = models.DateField(default=date.today)
#    date = models.DateField(auto_now_add=True)
