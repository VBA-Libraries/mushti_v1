from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Project, ProjectContribution
from .forms import ProjectCreateForm, ProjectContributionCreateForm
from django.forms.models import modelformset_factory
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

def project_edit_view(request,id,*args, **kwargs):
    project = Project.objects.get(id=id)
    form = ProjectCreateForm(request.POST or None, instance=project)
    rs = project.get_active_contributions()
    # print(rs)
    # form2 = ProjectContributionCreateForm(request.POST or None)
    proj_contrib_formset = modelformset_factory(model=ProjectContribution,form=ProjectContributionCreateForm,extra=0)
    form_set = proj_contrib_formset(request.POST or None,queryset=rs)

    context ={
        'object':project,
        'form': form,
        'form_set': form_set

    }

    if all([form.is_valid(), form_set.is_valid()]):
    # if form.is_valid():
        project =form.instance
        project.user = request.user
        form.save()
        for form in form_set:
            # child = form.save(commit=False)
            # child.project = project
            for form2 in form_set:
                contrib = form2.instance
                contrib.project = project
                form2.save()
        return redirect ('project:list_view')
    return render(request,'project/edit.html',context)

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


