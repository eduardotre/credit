from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model as user_model
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

from .forms import ApplicationForm
from .models import Application
from users.models import CustomUser

User = user_model()

# Create your views here.


def index(request):
    """ Home page"""
    return render(request, 'credit_apply/index.html')


def duplicate(request):
    return render(request, 'credit_apply/duplicate.html')


@login_required
def apply(request):
    """Submit application"""
    if request.method != 'POST':
        form = ApplicationForm()
    else:
        form = ApplicationForm(data=request.POST)
        if form.is_valid():
            try:
                app = Application.objects.get(owner=request.user)
                return redirect('credit_apply:duplicate')
            except ObjectDoesNotExist:
                try:
                    new_application = form.save(commit=False)
                    new_application.owner = request.user
                    new_application.save()
                    return redirect('credit_apply:submitted')
                except app.OtherError:
                    raise Http404("Error!")

    context = {'form': form}
    return render(request, 'credit_apply/apply.html', context)


def submitted(request):
    return render(request, 'credit_apply/submitted.html')


@login_required
def submission(request):
    """View submitted application"""
    try:
        application = Application.objects.get(owner=request.user)

        if request.method != 'POST':
            form = ApplicationForm(instance=application)
        else:
            form = ApplicationForm(instance=application, data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('credit_apply:submitted')
        context = {'application': application, 'form': form}
        return render(request, 'credit_apply/submission.html', context)
    except ObjectDoesNotExist:
        try:
            return redirect('credit_apply:index')
        except application.OtherError:
            raise Http404('Error!')


@login_required
def edit_application(request):
    """View submitted application"""
    application = Application.objects.get(owner=request.user)

    if request.method != 'POST':
        form = ApplicationForm(instance=application)
    else:
        form = ApplicationForm(instance=application, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('credit_apply:submitted')
    context = {'application': application, 'form': form}
    return render(request, 'credit_apply/edit_application.html', context)
