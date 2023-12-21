from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name='home'),
    path('books/',views.books,name='books'),
    path('author/',views.author,name='author'),
    path('addbook/',views.addbook,name="addbook"),
    path('aggregation_results/', views.aggregation_results, name='aggregation_results'),
    path('updatebook/<str:pk>/',views.updatebook,name="updatebook"),
    path('deletebook/<str:pk>/',views.deletebook,name="deletebook"),
   

    path('addauthor/',views.addauthor,name="addauthor"),
    
]
