from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('application_detail/', views.application_detail, name='application_detail')
]