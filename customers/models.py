from django.db import models

# Create your models here.


class Customer(models.Model):

    name = models.CharField (max_length=250)
    vat_id = models.CharField (max_length=15)
    street = models.CharField (max_length=250)
    city = models.CharField (max_length=100)
    country = models.CharField (max_length=100)

    class Meta:
        ordering = ['name']


    def __str__(self):
        return f'{self.name} ({self.vat_id})'
    