from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('books/', BooksView.as_view(), name='books'),
    path('authors/', AuthorsView.as_view(), name='authors'),
    path('book/add/', AddBookView.as_view(), name='add-book'),
    path('book/<int:pk>/update/', UpdateBookView.as_view(), name='update-book'),
    path('book/<int:pk>/delete/', DeleteBookView.as_view(), name='delete-book'),
    path('author/add/', AddAuthorView.as_view(), name='add-author'),
    path('author/<int:pk>/update/', UpdateAuthorView.as_view(), name='update-author'),
    path('author/<int:pk>/delete/', DeleteAuthorView.as_view(), name='delete-author'),
    path('aggregation/', AggregationResultsView.as_view(), name='aggregation-results'),
]

