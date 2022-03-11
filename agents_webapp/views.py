from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

# Create your views here.



def login(request):
    return render(request, 'agents_webapp/login.html')

@login_required
def dashboard(request):
    return render(request, 'agents_webapp/dashboard.html')


@login_required
def place_order(request):
    return render(request, 'agents_webapp/place_order.html')