from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth import get_user_model as user_model

User = user_model()
# Create your models here.


class Application(models.Model):
    INCOME_CHOICES = [
        ('low', '1000-10000'),
        ('med', '10001-20000'),
        ('high', '20001-40000'),
        ('vhigh', '40001-60000'),
        ('vvhigh', '60001+'),
    ]

    """App para las aplicacions de credito"""
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    business = models.CharField(max_length=100)
    m_number = PhoneNumberField(max_length=16)
    email = models.EmailField(max_length=254, unique=True)
    income = models.CharField(
        max_length=15, choices=INCOME_CHOICES, default='low')

    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.business}"
