from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .form import ProjectForm
# Create your views here.

def hello(request) :
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', { 'project':projects})
def saybye(request, pk):
    pk = pk
    idnumber = Project.objects.get(id = pk)
    return render(request, 'projects/project.html', {'project':idnumber})
def createform(request):
    form = ProjectForm()
    content = {'form': form}
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hello')
    return render(request, 'projects/project-form.html', content)

def updateform(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    content = {'form': form}
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('hello')
    return render(request, 'projects/project-form.html', content)

def deletetemplate(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('hello' )
    context =  {'object': project}
    return render(request, 'projects/delete-project.html', context)