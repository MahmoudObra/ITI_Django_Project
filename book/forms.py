from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['book_title','book_category','book_pages_num','book_date_of_publish','book_status']


class BookSearch(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['book_title']

