from django.http import request
from instagram.models import Image
from django.shortcuts import redirect, render
from django.http import HttpResponse


# Create your views here.
def home(request):
    allPhotos = Image.objects.all()
    title = "home"
    
    if request.method == "POST":
      igComment = request.POST.get('comment')
      print(igComment)

    context = {"images": allPhotos, "title": title}

    return render(request, "index.html", context)


# def comment(request):
#     igComment = request.POST.get("modaltextarea")
#     print(igComment)
#     return render(request, "index.html")