from django.shortcuts import render
from projects.models import Project,Contact

def home(request):
    return render(request, 'index.html', {}) #home page

def project_index(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.save()
        
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