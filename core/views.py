from django.shortcuts import render, redirect
from .models import Profile, Project, Testimonial
from .forms import ContactForm
from django.core.mail import send_mail

def home(request):
    profile = Profile.objects.first()
    testimonials = Testimonial.objects.all()
    return render(request, 'home.html', {'profile': profile, 'testimonials': testimonials})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(
                f'Message from {name} ({email})',
                message,
                email,  # Sender's email (client's)
                ['ankitasimkhada56@gmail.com'],  # Your email
                fail_silently=False,
            )
            
            return redirect('thank_you')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def thank_you(request):
    return render(request, 'thank_you.html')