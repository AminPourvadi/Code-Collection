from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Products(models.Model):
    name=models.CharField(max_length=20)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=5)
    image=models.ImageField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name

