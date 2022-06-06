from django.db import models

# Create your models here.
#people, address, product, doctor, bio
class Doctor(models.Model):
    specialisation= models.CharField(max_length=200)

    def __str__(self):
        return self.specialisation
    


class People(models.Model):
    full_name= models.CharField(max_length=200, default=1)
    age= models.PositiveIntegerField()
    health_challenge= models.CharField(max_length=200)
    patient= models.ForeignKey(Doctor, on_delete=models.PROTECT)

    def __str__(self):
        return self.full_name
    

class Address(models.Model):
    home_address= models.CharField(max_length=200)
    owner= models.OneToOneField(People, on_delete=models.CASCADE)

    def __str__(self):
        return self.owner
    


class Product(models.Model):
    product_category= models.CharField(max_length=200)
    product_name= models.CharField(max_length=200)
    product_price= models.PositiveIntegerField()

    def __str__(self):
        return self.product_name
    



class Bio(models.Model):
    your_bio= models.CharField(max_length=10000)
    user= models.OneToOneField(People, on_delete=models.CASCADE)

    def __str__(self):
        return self.user
    