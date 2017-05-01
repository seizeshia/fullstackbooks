from django.shortcuts import render, redirect

from .models import Books

def index(request):
    print Books
    context={
    "books": Books.objects.all()
    }

    return render(request, "first_app/index.html", context)

def adding(request):

    Books.objects.create(title=request.POST['title'], author=request.POST['author'], category=request.POST['category'])
    return redirect('/')
# Create your views here.
