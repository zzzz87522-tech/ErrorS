from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalog.models import Book, BookInstance


def index(request):
    """Домашняя страница приложения catalog."""
    return render(
        request,
        'index.html',
        context={
            'num_books': Book.objects.all().count(),
            'num_instances': BookInstance.objects.all().count(),
            'num_instances_available': BookInstance.objects.filter(status__exact='a').count(),
        }
    )


class BookListView(ListView):
    model = Book
    template_name = 'catalog/book_list.html'
    context_object_name = 'book_list'
    paginate_by = 10


class BookDetailView(DetailView):
    model = Book
    template_name = 'catalog/book_detail.html'
