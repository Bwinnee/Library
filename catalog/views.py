from django.shortcuts import render
from .models import Author, Book, BookInstance, Language, Genre
from django.views import generic

def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status="a").count()
    num_authors = Author.objects.count()
    num_sex_genres = Genre.objects.filter(name="erotica").count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        "num_books": num_books,
        "num_instances": num_instances,
        "num_instances_available": num_instances_available,
        "num_authors": num_authors,
        "num_sex_genres": num_sex_genres,
        "num_visits": num_visits,
    }
    return render(request, "index.html", context=context)


class BookListView(generic.ListView):
    model = Book
    template_name = "book_list.html"
    paginate_by = 4


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'


class AuthorListView(generic.ListView):
    model = Author
    template_name = "author_list.html"


class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = "author_detail.html"


# Create your views here.
