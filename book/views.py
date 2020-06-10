from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponse

from .models import Book

from .forms import BookForm , BookSearch


# Create your views here.
def index(request):
    return render(request,"index.html",{"key":"Mahmoud Amr"})


def searchBook(request):
    if request.method == 'POST' :
        searchFieldValue = BookSearch(request.POST)
        if searchFieldValue.is_valid() :
            name = searchFieldValue.cleaned_data['book_title']
            if name != '' and name is not None :
                try:
                    BookObj = get_object_or_404(Book , book_title=name)
                    context = {
                        'ABook' : BookObj ,
                    }
                    return render(request , 'readOnee.html' , context)
                    
                except :
                    return render(request,"indexx.html", {"key":"Sorry..Book cannot be found, Try again"})           
            else:
                return render(request,"indexx.html", {"key":""}) # if index.html , it will redirect to index.html in author

    else :
        form = BookSearch()
        context = {
            'form' : form ,
        }
        return render(request,"indexx.html", context)

############################################################################################333


# Read/Get All Books for the specific Author
def AllBooks(request):
    allBooks = Book.objects.all()

    context = {
        'allBooks' : allBooks ,
    }
    return render(request , 'readAll.html' , context)

# Read/Get specific Book
def ReadBook(request, id):
    ABook = get_object_or_404(Book , id=id)
    
    context = {
        'ABook' : ABook ,
    }
    return render(request, 'readOne.html' , context)


# Edit specific Book
def EditBook(request, id):
    ABook = get_object_or_404(Book , id=id)
    if request.method == 'POST' :
        form = BookForm(request.POST , instance=ABook)
        if form.is_valid():
            remainFieldsForm = form.save(commit=False)
            remainFieldsForm.book_author = request.user
            remainFieldsForm.save()
            return redirect('/')
        else:
            return redirect('/')

    else :
        form = BookForm(instance=ABook)
    
    context = {
        'form' : form ,
    }

    return render(request, 'edit.html', context)     


# Create/Insert Book Action/View

def createBook(request):
    if request.method == 'POST' :
        form = BookForm(request.POST)
        if form.is_valid():
            remainFieldsForm = form.save(commit=False)
            remainFieldsForm.book_author = request.user
            remainFieldsForm.save()
            return redirect('/')
        else:
            return redirect('/')


    else :
        form = BookForm()
    
    context = {
        'form' : form ,
    }

    return render(request, 'create.html', context) 


# Delete a Book
def DelBook(request, id):
    Book.objects.filter(id=id).delete()
    return redirect('/')
    