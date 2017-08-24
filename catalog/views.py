from django.shortcuts import render

# Create your views here.
from .models import Book, Author, BookInstance, Genre

def index(request):
    """
    view function for home page of site
    """
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    num_instances_available=BookInstance.objects.filter(status='a').count()
    num_authors=Author.objects.count()
    num_fictions=Genre.objects.filter(name='fiction').count()

    return render(request,'index.html',context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors,'num_fictions':num_fictions})