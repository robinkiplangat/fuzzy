from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Product(models.Model):
    type = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    ven = models.CharField(max_length=10)
    hfr = models.CharField(max_length=10)
    description = models.TextField(max_length=1000)
    uom = models.CharField(max_length=100)
    price = models.CharField(max_length=10)

    class Meta(object):
        """Meta options."""
        ordering = ["id"]

        def __str__(self):
            return self.code
