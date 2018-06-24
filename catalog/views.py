from django.shortcuts import render
from django.views import generic

from catalog.models import Book, BookInstance, Author, Genre


def index(request):
    genre = Genre.objects.all()
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Доступные книги (статус = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.all().count()

    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_instances': num_instances,
                 'num_instances_available': num_instances_available, 'num_authors': num_authors},
    )

class BookListView(generic.ListView):
    model = Book
    context_object_name = 'my_book_list'  # ваше собственное имя переменной контекста в шаблоне
    template_name = 'book_list.html'  # Определение имени вашего шаблона и его расположения

class BookDetailView(generic.DetailView):
    model = Book