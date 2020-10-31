from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    # price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, required=False)
    photo = models.ImageField(upload_to='products', blank=True)

    def __str__(self):
        return self.title
