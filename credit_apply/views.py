from django.shortcuts import render, redirect

from .forms import ApplicationForm

# Create your views here.


def index(request):
    """ Home page"""
    return render(request, 'credit_apply/index.html')


def apply(request):
    """Submit application"""
    if request.method != 'POST':
        form = ApplicationForm()
    else:
        form = ApplicationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('credit_apply:submitted')
    context = {'form': form}
    return render(request, 'credit_apply/apply.html', context)

def submitted(request):
    return render(request, 'credit_apply/submitted.html')
