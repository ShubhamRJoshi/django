from django.shortcuts import render
import json
import requests


# Create your views here.

def home(request):
    url = 'http://localhost:8000/u_api/projects'
    queryset_list = requests.get(url)
    project_doc = json.loads(queryset_list.text)
    project_data = []
    for k, v in project_doc['projects'].items():
        project_data.append(v)
    context = {
        'project_list': project_data,
    }
    return render(request, 'home.html', context)
