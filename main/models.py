from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    weapon = models.CharField(max_length=255)
    exterior = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    quality = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    quantity = models.IntegerField()

    @property
    def is_product_available(self):
        return self.quantity > 0
