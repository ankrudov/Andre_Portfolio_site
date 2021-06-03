from django.shortcuts import render
from projects.models import Project
from django.http import HttpResponse
from django.core.mail import send_mail

def home(request):
    return render(request, 'index.html', {}) #home page

def project_index(request):
    projects = Project.objects.all() #querying model data
    context = {
        'projects': projects
    }
    return render(request,'project_index.html',context)

def project_detail(request,pk):
    project = Project.objects.get(pk=pk) #retrives project with the primary key equal to that in function argument
    context = {
        'project': project
    }
    return render(request, 'project_detail.html',context)

def contact_me(request):
    if request.method == "POST":
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        
        #send email
        send_mail(
            subject + ' message from '+ name + surname, #subject
            message,#message
            email,#from email
            ['lpakaco@gmail.com','andre.vasquez.14@gmail.com'],#to email
        )
    
        return render(request, 'contact_index.html',{'name': name,})
     
    else:   
        return render(request,'contact_index.html',{})