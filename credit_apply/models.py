from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Application(models.Model):
    """App para las aplicacions de credito"""
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    business = models.CharField(max_length=100)
    m_number = PhoneNumberField(max_length=16 )
    email = models.EmailField(max_length=254, unique=True)

    date_added= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
