from django.shortcuts import render,redirect
from .models import *
from .forms import bookform , authorform
from django.db.models import Count, Avg, Max, Min
# Create your views here.
def home(request):

    authors = Author.objects.all()
    books = Book.objects.all()[5:]
    context = {
        'authors':authors,
        'books': books,
    }

    return render(request,"dashboard.html",context)


def books(request):
    books = Book.objects.all()
    return render(request,"books.html",{'books':books})


def author(request):
    authors = Author.objects.all()
    return render(request,"authors.html",{'authors':authors})

def addbook(request):
    form = bookform()
    if request.method == 'POST':
        form = bookform(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('/') 
    
    context = {'form':form}
    return render(request,"add_book.html",context)

def addauthor(request):
    form = authorform()
    if request.method == 'POST':
        form = authorform(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('/') 
    
    context = {'form':form}
    return render(request,"add_author.html",context)


def updatebook(request,pk):
    book = Book.objects.get(id=pk)
    form =bookform(instance=book)
    if request.method == 'POST':
        form = bookform(request.POST,instance=book)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('/') 
    context ={
        'form':form,
    }
    return render(request,'add_book.html',context)

def deletebook(request,pk):
    book = Book.objects.get(id=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('/')
    context={"item":book}
    return render(request,'delete.html',context)

def aggregation_results(request):
    total_books = Book.objects.count()
    average_price = Book.objects.aggregate(Avg('price'))['price__avg']
    oldest_book = Book.objects.order_by('publication_year').first()
    newest_book = Book.objects.order_by('-publication_year').first()
    books_published_each_year = Book.objects.values('publication_year').annotate(count=Count('id'))

    authors = Author.objects.all()  # You might need authors for the existing part of the template

    context = {
        'total_books': total_books,
        'average_price': average_price,
        'oldest_book': oldest_book,
        'newest_book': newest_book,
        'books_published_each_year': books_published_each_year,
        'authors': authors,  # You might need authors for the existing part of the template
    }
    return render(request, 'aggregation.html', context)