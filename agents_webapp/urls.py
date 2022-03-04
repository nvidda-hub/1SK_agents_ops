from django.urls import path
from agents_webapp import views
from agents_webapp.forms import LoginForm
from django.contrib.auth import views as auth_views

app_name = "agents_webapp"

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='agents_webapp/login.html', authentication_form=LoginForm), name='login'),
    path('dashboard/', views.dashboard, name="dashboard"),
]
