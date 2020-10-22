from django.http import request
from instagram.models import Comment, Image
from django.shortcuts import redirect, render
from django.http import HttpResponse


# Create your views here.
def home(request):
    allPhotos = Image.objects.all()
    title = "home"

    if request.method == "POST":
        # igComment = request.POST.get('comment')
        form = request.POST
        postedComment = form.get('comment')

        comment = Image(comment=postedComment)
        comment.save()

    context = {"images": allPhotos, "title": title}

    return render(request, "index.html", context)


# def comment(request):
#     igComment = request.POST.get("modaltextarea")
#     print(igComment)
#     return render(request, "index.html")