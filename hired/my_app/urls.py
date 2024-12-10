# from django.urls import path, include
# from . import views
# from django.contrib.auth import views as auth_views
# from .views import DashboardView


# urlpatterns = [
#     path('', views.Home.as_view(), name='home'),  # Home page
#     path('about/', views.about, name='about'),    # About page
#     path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard page
#     path('application/<int:id>/', views.application_detail, name='application_detail'),  # Application detail page
#     path('create/', views.create_application, name='create'),  # Add an Application
#     path('accounts/', include('django.contrib.auth.urls')),  # Authentication URLs (login/logout)
#     path('accounts/signup/', views.signup, name='signup'),  # Sign-up page
    
    
#     path('update/<int:id>/', views.update_application, name='update'),  # Update page
#     path('delete/<int:id>/', views.delete_application, name='delete'),  # Delete page
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),  # Home page
    path('about/', views.about, name='about'),    # About page
    path('dashboard/', views.JobApplicationListView.as_view(), name='dashboard'),  # Job Application ListView
    path('application/<int:pk>/', views.JobApplicationDetailView.as_view(), name='application_detail'),  # Job Application DetailView
    path('create/', views.JobApplicationCreateView.as_view(), name='create'),  # Job Application CreateView
    path('update/<int:pk>/', views.JobApplicationUpdateView.as_view(), name='update'),  # Job Application UpdateView
    path('delete/<int:pk>/', views.JobApplicationDeleteView.as_view(), name='delete'),  # Job Application DeleteView
    path('accounts/signup/', views.signup, name='signup'),  # Sign-up page
]
