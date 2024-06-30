from django.urls import path
from . import views

app_name = "playground"
urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/<str:id>', views.dashboard, name='dashboard'),
]