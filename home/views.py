from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello world!")
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')


# Create your views here.
def sign_in(request):
    return render(request,"sign_in.html")

def sign_up(request):
    return render(request,"sign_up.html")