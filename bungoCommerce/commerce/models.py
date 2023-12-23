# pyright: reportGeneralTypeIssues=false

from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField(verbose_name="price", default=0.0)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return f"{self.name}: the price is {self.price}"
