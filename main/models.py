from django.db import models
import uuid
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
    name = models.CharField(max_length=255)
    weapon = models.CharField(max_length=255)
    exterior = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    quality = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    quantity = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateField(auto_now_add=True) 

    @property
    def is_product_available(self):
        return self.quantity > 0
