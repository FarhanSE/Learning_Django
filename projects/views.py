from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .form import ProjectForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def hello(request) :
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', { 'project':projects})
def saybye(request, pk):
    pk = pk
    idnumber = Project.objects.get(id = pk)
    return render(request, 'projects/project.html', {'project':idnumber})
@login_required(login_url='login')
def createform(request):
    form = ProjectForm()
    content = {'form': form}
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app')
    return render(request, 'projects/project-form.html', content)


@login_required(login_url='login')
def updateform(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    content = {'form': form}
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES,  instance=project)
        if form.is_valid():
            form.save()
            return redirect('app')
    return render(request, 'projects/project-form.html', content)


@login_required(login_url='login')
def deletetemplate(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('app' )
    context =  {'object': project}
    return render(request, 'projects/delete-project.html', context)