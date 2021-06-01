from django.shortcuts import render
from projects.models import Project

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