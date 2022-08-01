from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Project
from .forms import ProjectCreateForm
# Create your views here.

def project_list_view(request,*args, **kwargs):
    qs = Project.objects.get_all_active_projects()
    context ={
        'object_list': qs
    }
    return render(request,'project/list.html',context)


def project_detail_view(request,id,*args, **kwargs):
    project = Project.objects.get(id=id)
    context ={
        'object':project
    }
    return render(request,'project/detail.html',context)

def project_create_view(request,*args, **kwargs):
    form = ProjectCreateForm(request.POST or None)
    context = {
        'form':form
    }
    if form.is_valid():
        project =form.instance
        project.user = request.user
        form.save()
        return redirect ('project:list_view')
    return render(request,'project/create.html',context)


