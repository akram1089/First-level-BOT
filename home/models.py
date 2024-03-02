from django.db import models

# Create your models here.



from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=150, null=True , blank=True)


    full_name=models.CharField( max_length=50,null=True,blank=True)
    email=models.EmailField( max_length=254,blank=True)
    Mobile_number=models.CharField( max_length=50,unique=True)
    Phone_code=models.CharField( max_length=50,null=True,blank=True)
    password=models.CharField( max_length=500,null=True,blank=True)
    confirm_password=models.CharField( max_length=50,null=True,blank=True)
    Country=models.CharField( max_length=50,null=True,blank=True)
    State=models.CharField( max_length=50,null=True,blank=True)
    forget_password_token = models.CharField(max_length=100,null=True)
    terms_of_service = models.BooleanField(default=False)
    secret_key = models.CharField(max_length=50, blank=True, null=True)
    ip_address_user = models.CharField(max_length=50, blank=True, null=True)  # Add this field


    objects=UserManager()
    USERNAME_FIELD='Mobile_number'
    REQUIRED_FIELDS=[]



class Broker(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    broker_name = models.CharField(max_length=255)
    trading_platform = models.CharField(max_length=255)
    logging_id = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    totp_key = models.CharField(max_length=255)
    fa_pin = models.CharField(max_length=6)
    phone_number = models.CharField(max_length=15)
    api_key = models.CharField(max_length=255)
    api_secret = models.CharField(max_length=255)
    app_name = models.CharField(max_length=255)
    enctoken=models.TextField()
    active_api = models.BooleanField(default=False)
    advance_totp_security = models.BooleanField(default=False)  # New field

    added_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return f"{self.broker_name} - {self.user} - {self.app_name}"
    
