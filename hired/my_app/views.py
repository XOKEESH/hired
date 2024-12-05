from django.shortcuts import render, get_object_or_404, redirect
from .forms import JobApplicationForm
from .models import JobApplication

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dashboard(request):
    applications = JobApplication.objects.all()
    return render(request, 'dashboard.html', {'applications': applications})

# def application_detail(request, id):
#     application = get_object_or_404(JobApplication, id=id)
#     return render(request, 'application_detail.html', {'application': application})

def application_detail(request, id):
    application = get_object_or_404(JobApplication, id=id)
    return render(request, 'application_detail.html', {'application': application})

def create_application(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = JobApplicationForm()
    return render(request, 'create.html', {'form': form})

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

def delete_application(request, id):
    application = get_object_or_404(JobApplication, id=id)
    if request.method == 'POST':
        application.delete()
        return redirect('dashboard')
    return render(request, 'delete.html', {'application': application})