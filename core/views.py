from django.shortcuts import render
from .models import Contact
# Create your views here.
def home(request):
    context = {'home':'active'}
    return render(request,'core/home.html',context)

def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        contact=Contact(name=name,email=email,subject=subject,message=message)
        contact.save()
    context = {'contact':'active'}
    return render(request,'core/contact.html',context)


    