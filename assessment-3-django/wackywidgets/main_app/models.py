from django.db import models

# Create your models here.
class Widgets(models.Model):
    description = models.CharField('Description', max_length=100)
    quantity = models.IntegerField('Quantity')