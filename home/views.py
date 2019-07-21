from django.shortcuts import render
from django.conf import settings


# Create your views here.

def home(request):

    your_media_root = settings.MEDIA_ROOT

    # name = file_path.file.name
    # url = file_path.file.url
    # path = file_path.file.path
    print(your_media_root)
    # print(name)
    # print(url)
    # print(path)
    return render(request, 'home.html')
