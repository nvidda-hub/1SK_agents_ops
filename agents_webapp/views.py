from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


def login(request):
    return render(request, 'agents_webapp/login.html')

@login_required
def home(request):
    print(request.user.is_authenticated)
    return render(request, 'agents_webapp/home.html')