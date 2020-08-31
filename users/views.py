from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import EmailSignUp
# Create your views here.


def register(request):
    if request.method != 'POST':
        form = EmailSignUp()
    else:
        form = EmailSignUp(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('credit_apply:index')
    context = {'form': form}
    return render(request, 'registration/register.html', context)
