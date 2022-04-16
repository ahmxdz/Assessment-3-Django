from django.db import models
from django.urls import reverse
# Create your models here.
class Widgets(models.Model):
    description = models.CharField('Description', max_length=100)
    quantity = models.IntegerField('Quantity')

    def get_absolute_url(self):
        return reverse('add_widgets')