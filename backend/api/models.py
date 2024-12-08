from django.db import models

# Create your models here.

class InterestForm(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField((""), max_length=254)
    product = models.CharField(max_length=10)
    created_at = models.DateField(auto_now_add=True)


class ProductStats(models.Model):
    product = models.CharField(max_length=20)
    volume = models.DecimalField(max_digits=20, decimal_places=8)  # Increase total digits
    last = models.DecimalField(max_digits=15, decimal_places=2)   # Adjust for monetary values
    high = models.DecimalField(max_digits=15, decimal_places=2)
    low = models.DecimalField(max_digits=15, decimal_places=2)