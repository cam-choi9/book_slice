from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *

from .slice import *

# Create your views here.
def main(request):
    return HttpResponse("<h1>Hello</h1>")


def upload(request):

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            print(type(obj.page))

            return render(request, 'books/upload.html', {"obj": obj})
    else:
        form = BookForm()

    page = Book.objects.all()
    return render(request, 'books/upload.html', {"page": page, "form": form})


def view(request):
    pages = Book.objects.all()

    context = {'view': pages}

    return render(request, 'books/view.html', context)


