from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .forms import EmailSignUp
from .models import CustomUser

admin.site.register(CustomUser)
