from django.shortcuts import render
from home.models import Contact

def home(request):
    return render(request, 'index.html')

def contact(request):
    if request.method=="POST":
        firstname=request.POST.get('fname')
        lastname=request.POST.get('lname')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        new_contact=Contact(FirstName=firstname,LastName=lastname,Email=email,Subject=subject,Message=message)
        new_contact.save()
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def blog(request):
    return render(request, 'blog.html')

def sign_up(request):
    return render(request, 'sign_up.html')

def sign_in(request):
    return render(request, 'sign_in.html')

