from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponse

from .models import Author

from book.models import Book

from .forms import AuthorForm , AuthorSearch


# Create your views here.
def index(request):
    if request.method == 'POST' :
        searchFieldValue = AuthorSearch(request.POST)
        #name = searchFieldValue.save(commit=False).author_name
        if searchFieldValue.is_valid() :
            name = searchFieldValue.cleaned_data['author_name']
            # name = request.POST.get('author_input') # if there is a textfield created in html 
            if name != '' and name is not None :
                #AuthObj = Author.objects.get(author_name=name)
                try:
                    AuthObj = get_object_or_404(Author , author_name=name)
                    context = {
                        'AnAuth' : AuthObj ,
                    }
                    return render(request , 'readOne.html' , context)
                    
                except :
                    return render(request,"index.html", {"key":"Sorry..Author cannot be found, Try again"})           
            else:
                return render(request,"index.html", {"key":""})

    else :
        form = AuthorSearch()
        context = {
            'form' : form ,
        }
        return render(request,"index.html", context)


'''
# Create your views here.
def index(request):

    form = AuthorSearch()
    context = {
        'form' : form ,
    }
    return render(request,"index.html", context)
'''

# Search for Author
'''
def searchAuthor(request , authName):
    AnAuth = Author.objects.get(author_name=authName)
    if AnAuth != null :
        context = {
            'AnAuth' : AnAuth ,
        }
        return render(request , 'readOne.html' , context)
    
    else :
        return render(request,"index.html", {"key":"Sorry..Author cannot be found, Try again"})
'''

# Search for Author # Became not used

def searchAuthor(request , authName):
    AnAuth = Author.objects.get(author_name=authName)
    if AnAuth != null :
        form = AuthorSearch(instance=AnAuth)
        context = {
            'form' : form ,
        }
        return render(request , 'readOne.html' , context)
    
    else :
        return render(request,"index.html", {"key":"Sorry..Author cannot be found, Try again"})

##########################################################################################





##########################################################################################
# Read/Get All Authors for the loged in user
def AllAuthors(request):
    allAuth = Author.objects.all()

    context = {
        'allAuth' : allAuth ,
    }
    return render(request , 'readAll.html' , context)

# Read/Get specific Author
def ReadAuthor(request, id):
   # AnAuth = Author.objects.get(id=id)   # as we want to show 404 error if id isn't found, we will use the next line
    AnAuth = get_object_or_404(Author , id=id)
    
    context = {
        'AnAuth' : AnAuth ,
    }
    return render(request, 'readOne.html' , context)


# Edit specific Author
def EditAuthor(request, id):
    AnAuth = get_object_or_404(Author , id=id)
    if request.method == 'POST' :
        form = AuthorForm(request.POST , instance=AnAuth)
        if form.is_valid():
            remainFieldsForm = form.save(commit=False)
            remainFieldsForm.author_user = request.user
            remainFieldsForm.save()
            return redirect('/')
        else:
            return redirect('/')

    else :
        form = AuthorForm(instance=AnAuth)
    
    context = {
        'form' : form ,
    }

    return render(request, 'edit.html', context)     


# Create/Insert Author Action/View

def createAuthor(request):
    if request.method == 'POST' :
        form = AuthorForm(request.POST)
        if form.is_valid():
            remainFieldsForm = form.save(commit=False)
            remainFieldsForm.author_user = request.user
            remainFieldsForm.save()
            return redirect('/')
        else:
            return redirect('/')


    else :
        form = AuthorForm()
    
    context = {
        'form' : form ,
    }

    return render(request, 'create.html', context) 


# Delete an Author
def DelAuthor(request, id):
    Author.objects.filter(id=id).delete()
    return redirect('/')

    #instance = SomeModel.objects.get(id=id)
    #instance.delete()