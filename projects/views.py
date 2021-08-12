from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
projectlist = [
    {
        'id': 1,
        'title': 'Ecommerce',
        'description': 'fully functiona ecommerce website'
    }, 
    {
        'id': 2,
        'title': 'Portfolio',
        'description': 'This was the project where i built out my portfolio'
    },
    {
        'id': 3,
        'title': 'Social Network',
        'description': 'Awesome open source projects'
    }
]
def hello(request) :
    name = "Farhan"
    number = 10
    return render(request, 'projects/projects.html', {"name":name, "number":number, 'project':projectlist})
def saybye(request, pk):
    idnumber = None
    for i in projectlist:
        if i['id'] == pk:
            idnumber = i
    return render(request, 'projects/project.html', {'project':idnumber})