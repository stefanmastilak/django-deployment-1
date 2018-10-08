from django.urls import path
from base_app import views

# Template URLS!
app_name = 'base_app'

urlpatterns = [
    path('register/', views.registerView, name="register"),
    path('user_login/', views.user_loginView, name="user_login"),
]
