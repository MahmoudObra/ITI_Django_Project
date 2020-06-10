from django import forms
from .models import Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['author_name','author_age','author_nationality','author_phone_number']


class AuthorSearch(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['author_name']