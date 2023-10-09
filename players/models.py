from django.db import models
from passlib.hash import pbkdf2_sha256


# Create your models here.
class RegisterUser(models.Model):
    account_type_choices = [
        ('A', 'Administrator'),
        ('P', 'Player')
    ]
    user_id = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=255, blank=True)
    identity = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    mobile_number = models.CharField(max_length=20, blank=True)
    whatsapp_number = models.CharField(max_length=20, blank=True)
    account_type = models.CharField(max_length=10, choices=account_type_choices, default='A')

    def verify_password(self, password):
        return pbkdf2_sha256.verify(password, self.password)
    
