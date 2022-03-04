from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

# Create your views here.



@login_required
def dashboard(request):
    print(request.user.is_authenticated)
    return render(request, 'agents_webapp/dashboard.html')