from distutils.command import upload
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ImageField(blank=False, null=False)
    Name = models.CharField(max_length=200)
    about = models.CharField(max_length=300)
    is_hiring  = models.BooleanField()

    def __str__(self):
        return self.Name

    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url = ''
        return url

class Application(models.Model):
    profile = models.ImageField(upload_to='find\static\site\images')
    Full_name = models.CharField(max_length=200)
    Age = models.IntegerField(default=18)
    Residence = models.CharField(max_length=200)
    number = models.BigIntegerField()
    email = models.EmailField()
    Cv = models.FileField(upload_to='documents/')
    bio = models.TextField()

    def __str__(self):
        return self.Full_name

class Individual(models.Model):
    Full_name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    job_descr =  models.CharField(max_length=200)
    amount_due = models.IntegerField(default="$200")
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.job_title

class Payment(models.Model):
    CARDS = (
        ('visa','visa'),
        ('mastercard','mastercard'),
    )
    Name_On_Card = models.CharField(max_length=200)
    Card_Number = models.BigIntegerField()
    CVC = models.BigIntegerField()
    card_type = models.CharField(choices=CARDS,max_length=200)
    address = models.CharField(max_length=200)
    
    def __str__(self):
        self.Name_On_Card 
