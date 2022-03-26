from django.shortcuts import render

# Create your views here.
from .models import Contact


# 會與 contact.html 相對應!!

def contact(request):
    
    if 'name' in request.POST:
        
        name = request.POST['name']
       
        email = request.POST['email']
        
        subject = request.POST['subject']
        
        message = request.POST['message']
             
        
        obj=Contact.objects.create(name = name,email = email,subject = subject,content = message)
        obj.save()


    return render(request,'contact.html')
