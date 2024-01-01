from django.views.generic import ListView, CreateView, UpdateView, DeleteView,TemplateView
from django.urls import reverse_lazy
from .models import Book, Author
from .forms import bookform, authorform
from django.db.models import Count, Avg

class HomeView(ListView):
    template_name = 'dashboard.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.all()[5:]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = Author.objects.all()
        return context

class BooksView(ListView):
    model = Book
    template_name = 'books.html'
    context_object_name = 'books'

class AuthorsView(ListView):
    model = Author
    template_name = 'authors.html'
    context_object_name = 'authors'

class AddBookView(CreateView):
    model = Book
    form_class = bookform
    template_name = 'add_book.html'
    success_url = reverse_lazy('home')

class UpdateBookView(UpdateView):
    model = Book
    form_class = bookform
    template_name = 'add_book.html'
    success_url = reverse_lazy('home')

class DeleteBookView(DeleteView):
    model = Book
    template_name = 'delete.html'
    success_url = reverse_lazy('home')

class AddAuthorView(CreateView):
    model = Author
    form_class = authorform
    template_name = 'add_author.html'
    success_url = reverse_lazy('home')

class UpdateAuthorView(UpdateView):
    model = Author
    form_class = authorform
    template_name = 'add_author.html'
    success_url = reverse_lazy('home')

class DeleteAuthorView(DeleteView):
    model = Author
    template_name = 'delete.html'
    success_url = reverse_lazy('home')

class AggregationResultsView(TemplateView):
    template_name = 'aggregation.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['total_books'] = Book.objects.count()
        context['average_price'] = Book.objects.aggregate(Avg('price'))['price__avg']
        context['oldest_book'] = Book.objects.order_by('publication_year').first()
        context['newest_book'] = Book.objects.order_by('-publication_year').first()
        context['books_published_each_year'] = Book.objects.values('publication_year').annotate(count=Count('id'))

        return context