from django.urls import path
from agents_webapp import views
from agents_webapp.forms import LoginForm
from django.contrib.auth import views as auth_views

app_name = "agents_webapp"

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(template_name='agents_webapp/login.html', authentication_form=LoginForm), name='login'),
    path('', views.dashboard, name="dashboard"),
    path('place/order/', views.place_order, name="place_order"),
    path('logout/', auth_views.LogoutView.as_view(next_page='agents_webapp:dashboard'), name='logout'),
    
]
