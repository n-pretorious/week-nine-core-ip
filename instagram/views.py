from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import request
from instagram.models import Comment, Image
from django.shortcuts import redirect, render
from django.http import HttpResponse



# Create your views here.
def home(request):

    context = {"images": allPhotos, "title": title}
    
    return render(request, "index.html", context)


def profile(request):
    allPhotos = Image.objects.all()
    title = "profile"

    if request.method == "POST":
        image = Image()

        form = request.POST

        image.comment = form.get("comment")
        image.save()

        if form.get("like"):
            print(image.noOfLikes)
            image.noOfLikes += 1
            image.save()

    context = {"images": allPhotos, "title": title}

    return render(request, "index.html", context)


# def comment(request):
#     igComment = request.POST.get("modaltextarea")
#     print(igComment)
#     return render(request, "index.html")

def logout_view(request):
    logout(request)