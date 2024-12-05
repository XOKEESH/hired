from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('about/', views.about, name='about'),  # About page
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard page
    path('application/<int:id>/', views.application_detail, name='application_detail'),  # Application detail page
    path('create/', views.create_application, name='create'),  # Create page
    path('update/<int:id>/', views.update_application, name='update'),  # Update page
    path('delete/<int:id>/', views.delete_application, name='delete'),  # Delete page
]