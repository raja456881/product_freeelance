from django.db import models
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='product/image',blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)


    def __str__(self):
        return  self.name