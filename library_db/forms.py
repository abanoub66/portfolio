from django import forms
from . import models


class CreateLibraryUser(forms.ModelForm):
    class Meta:
        model = models.LibraryUser
        fields = ['first_name', 'last_name', 'birthdate']


class CreateBook(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = ['title', 'author', 'publisher', 'publish_date', 'number_of_pages']
