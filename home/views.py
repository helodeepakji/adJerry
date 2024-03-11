from django.shortcuts import render,redirect
from home.models import Contact
from django.contrib.auth.models import User

def home(request):
    return render(request, 'index.html')

def contact(request):
    if request.method=="POST":
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        new_contact = Contact(FirstName=firstname,LastName=lastname,Email=email,Subject=subject,Message=message)
        new_contact.save()
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def blog(request):
    return render(request, 'blog.html')

def sign_up(request):
    if request.method=="POST":
        firstname=request.POST.get('fname')
        lastname=request.POST.get('lname')
        email=request.POST.get('email') 
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        if not (firstname and lastname and email and password and cpassword):
            return render(request, 'signup.html', {'error_message': 'All fields are required'})
        if password != cpassword:
            return render(request, 'signup.html', {'error_message': 'Passwords do not match'})
        if User.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error_message': 'Email already exists'})
        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = firstname
        user.last_name = lastname
        user.save()
        return redirect('sign_in')
    return render(request, 'sign_up.html')

def sign_in(request):
    return render(request, 'sign_in.html')

