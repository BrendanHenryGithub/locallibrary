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
    num_visits=request.session.get('num_visits',0)
    request.session['num_visits']=num_visits+1

    return render(request,'index.html',context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors,'num_fictions':num_fictions,'num_visits':num_visits})

from django.views import generic

class BookListView(generic.ListView):
    model = Book

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author

class AuthorDetailView(generic.DetailView):
    model = Author
