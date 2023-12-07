from django.db import models
class ProductData(models.Model):
    category=models.CharField(max_length=100)
    def __str__(self):
        return self.category

class Product(models.Model):
    pid=models.IntegerField()
    product=models.CharField(max_length=100)
    date=models.DateField()
    price=models.DecimalField(max_digits=6,decimal_places=2)
    category=models.ForeignKey(ProductData,on_delete=models.CASCADE)

    def __str__(self):
        return self.product
