from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Configuration(models.Model):
    key = models.CharField(max_length=100)
    value = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.key
    
    def table(self):
        return 'configuration'

    def __str__(self):
        return self.key

class CustomUser(AbstractUser):
    id_business = models.ForeignKey('Business', on_delete=models.SET_NULL, null=True, blank=True, db_column='business_id')
    bio = models.TextField(max_length=500, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=100, blank=True)
    comune = models.CharField(max_length=100, blank=True)
    corporative_email = models.EmailField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
    nacionality = models.CharField(max_length=100, blank=True)
    marital_status = models.CharField(max_length=100, blank=True)
    gender = models.IntegerField(choices=((0, 'Masculino'), (1, 'Femenino'), (2, 'Otro')), default=0)

    def save(self, *args, **kwargs):
        if self.email:
            self.email = self.email.lower()

            if not self.username:
                self.username = self.email
        else:
            raise ValueError('El email es obligatorio')
            
        return super(CustomUser, self).save(*args, **kwargs)

    def __str__(self):
        return self.username
    
class Business(models.Model):
    name = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    address = models.CharField(max_length=100)
    region = models.CharField(max_length=100, null=True, blank=True)
    province = models.CharField(max_length=100, null=True, blank=True)
    commune = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

class BusinessMeta(models.Model):
    business_id = models.ForeignKey(Business, on_delete=models.CASCADE)
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100) 

    def __str__(self):
        return self.value
    
class CustomUserMeta(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100) 

    def __str__(self):
        return self.value
    
class BankAccount(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    bank = models.CharField(max_length=100)
    account_number = models.CharField(max_length=100)
    account_type = models.CharField(max_length=100)
    rut = models.CharField(max_length=12)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.bank} - {self.account_number}"