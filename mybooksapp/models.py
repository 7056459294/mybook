from django.db import models

# Create your models here.
class books(models.Model):
    book_id=models.AutoField
    book_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50, default="")
    price=models.IntegerField( default=0)
    des=models.CharField(max_length=(300))
    image=models.ImageField(upload_to="shop/image" , default="")
    
    
    def __str__(self):
        return self.book_name   

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name

class users(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    Address= models.CharField(max_length=100, default="")
    phone_no= models.CharField(max_length=12, default="")
    password=models.CharField(max_length=100, default="")
    usertype=models.CharField(max_length=100, default="")
    
   
    def __str__(self):
          return self.email 

class soldbooks(models.Model):
    book_name=models.CharField(max_length=50)
    cus_name=models.CharField(max_length=50)
    cus_email=models.CharField(max_length=50)
    price=models.IntegerField( default=0)

    def __str__(self):
      return self.cus_email 