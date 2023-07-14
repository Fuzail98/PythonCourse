from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=120)  # max_length = required
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField(default="This is a product.")
    testField = models.BooleanField(null=True)

    def __str__(self):
        return self.title
