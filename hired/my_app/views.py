# from django.shortcuts import render, get_object_or_404, redirect
# from .forms import JobApplicationForm
# from .models import JobApplication
# from django.contrib.auth import login
# from django.contrib.auth.views import LoginView
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.generic import TemplateView, ListView



# # Create your views here.
# class Home(LoginView):
#     template_name = 'home.html'

# def about(request):
#     return render(request, 'about.html')

# def dashboard(request):
#     applications = JobApplication.objects.all()
#     return render(request, 'dashboard.html', {'applications': applications})

# def application_detail(request, id):
#     application = get_object_or_404(JobApplication, id=id)
#     return render(request, 'application_detail.html', {'application': application})

# @login_required
# def create_application(request):
#     if request.method == 'POST':
#         form = JobApplicationForm(request.POST)
#         if form.is_valid():
#             application = form.save(commit=False)  # Don't save to DB yet
#             application.user = request.user  # Set the logged-in user
#             application.save()  # Save the instance with the user attached
#             return redirect('dashboard')  # Redirect to the dashboard
#     else:
#         form = JobApplicationForm()
#     return render(request, 'create.html', {'form': form})

# def update_application(request, id):
#     application = get_object_or_404(JobApplication, id=id)
#     if request.method == 'POST':
#         form = JobApplicationForm(request.POST, instance=application)
#         if form.is_valid():
#             form.save()
#             return redirect('dashboard')
#     else:
#         form = JobApplicationForm(instance=application)
#     return render(request, 'update.html', {'form': form})

# def delete_application(request, id):
#     application = get_object_or_404(JobApplication, id=id)
#     if request.method == 'POST':
#         application.delete()
#         return redirect('dashboard')
#     return render(request, 'delete.html', {'application': application})

# def signup(request):
#     error_message = ''
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()  # Create the user
#             login(request, user)  # Automatically log in the user
#             return redirect('dashboard')  # Redirect to the cat index page
#         else:
#             error_message = 'Invalid sign up - try again'
#     else:
#         form = UserCreationForm()  # Create an empty form for GET request

#     context = {'form': form, 'error_message': error_message}
#     return render(request, 'signup.html', context)

# from django.shortcuts import render
# from .models import JobApplication

# @login_required
# def dashboard(request):
#     job_applications = JobApplication.objects.filter(user=request.user)
#     return render(request, 'dashboard.html', {'job_applications': job_applications})

# class DashboardView(LoginRequiredMixin, TemplateView):
#     model = JobApplication
#     template_name = 'dashboard.html'


from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from .models import JobApplication
from .forms import JobApplicationForm

# Create your views here.
class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

# @login_required
# def dashboard(request):
#     job_applications = JobApplication.objects.filter(user=request.user)
#     return render(request, 'dashboard.html', {'job_applications': job_applications})

@login_required
def application_detail(request, id):
    application = get_object_or_404(JobApplication, id=id)
    return render(request, 'application_detail.html', {'application': application})

@login_required
def create_application(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()
            return redirect('dashboard')
    else:
        form = JobApplicationForm()
    return render(request, 'create.html', {'form': form})

@login_required
def update_application(request, id):
    application = get_object_or_404(JobApplication, id=id)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = JobApplicationForm(instance=application)
    return render(request, 'update.html', {'form': form})

@login_required
def delete_application(request, id):
    application = get_object_or_404(JobApplication, id=id)
    if request.method == 'POST':
        application.delete()
        return redirect('dashboard')
    return render(request, 'delete.html', {'application': application})

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

class JobApplicationCreateView(LoginRequiredMixin, CreateView):
    model = JobApplication
    fields = [
        'job_title', 
        'company_name', 
        'status', 
        'job_link', 
        'job_description', 
        'notes', 
        'attachments'
    ]

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)

    success_url = '/dashboard/' 
    template_name = 'create.html'

class JobApplicationUpdateView(LoginRequiredMixin, UpdateView):
    model = JobApplication
    form_class = JobApplicationForm
    success_url = 'dashboard.html'

class JobApplicationDeleteView(LoginRequiredMixin, DeleteView):
    model = JobApplication
    success_url = 'dashboard.html'

class JobApplicationListView(LoginRequiredMixin, ListView):
    model = JobApplication
    template_name = 'dashboard.html'
    context_object_name = 'job_applications'

    def get_queryset(self):
        return JobApplication.objects.filter(user=self.request.user)

class JobApplicationDetailView(LoginRequiredMixin, DetailView):
    model = JobApplication
    template_name = 'application_detail.html'
    context_object_name = 'job_application'