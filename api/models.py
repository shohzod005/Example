from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField()
    desc  = models.TextField()

    def __str__(self) -> str:
        return self.name



class Product(models.Model):
    product = models.ManyToManyField(to=Category)
    name = models.TextField()
    slug = models.SlugField()
    desc = models.TextField()
    price = models.PositiveIntegerField()
    
    def __str__(self) -> str:
        return self.name

class Inventory(models.Model):
    category = models.ForeignKey(to=Product,on_delete=models.CASCADE)
    status  = models.BooleanField(default=True)
    quen = models.PositiveIntegerField()
    
    def __str__(self) -> str:
        return self.category


class product_photo(models.Model):
    product = models.ForeignKey(to=Product,on_delete=models.CASCADE)
    thumb  = models.ImageField(upload_to="media/image")
    lorg_pc = models.ImageField(upload_to="media/image")

    def __str__(self) -> str:
        return self.product


class CostumUser(models.Model):
    fullnamne = models.TextField()
    email  = models.EmailField(max_length=250,unique=True)
    phone_number = models.CharField(max_length=30)
    address = models.CharField(max_length=30)

    
    def __str__(self) -> str:
        return self.fullnamne

class order(models.Model):
    custmuser = models.ForeignKey(to=CostumUser,on_delete=models.CASCADE)
    product = models.ManyToManyField(to=Product)
    totol_price = models.PositiveIntegerField()
    
    def __str__(self) -> str:
        return self.custmuser


