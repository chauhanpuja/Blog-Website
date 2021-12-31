from django.db import models
from django.db.models.fields.files import ImageField
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Product(models.Model):
    id=models.AutoField(primary_key=True)
    pro_name=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    desc=models.CharField(max_length=500)
    price=models.IntegerField()
    image=ImageField(upload_to='shop/img')
    date = models.DateField()

    def __str__(self):
        return self.pro_name

class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=500)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")

    def __str__(self):
        return self.name


class Contact(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=200,default="")
    desc=models.CharField(max_length=500,default="")

    def __str__(self):
        return self.name




class Comment(models.Model):
    sno= models.AutoField(primary_key=True)
    comments=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp= models.DateTimeField(default=now)

    def __str__(self):
        return self.comments + "..." + "by " + " " + self.user.username
