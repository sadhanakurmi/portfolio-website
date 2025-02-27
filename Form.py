from django import forms
from .models import Book

class BookForm(forms.modelForm):
    class Meta:
        model = Book
        fields = ['title','author','published_date','isbn']
        
