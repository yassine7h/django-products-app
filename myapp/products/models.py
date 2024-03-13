from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(default=0.)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Name : {self.name}, price : {self.price}, category : {self.category.name if self.category is not None else "No Category"}"
