from django.forms import ModelForm, CharField, ImageField, TextInput, FileInput, DateInput, Textarea, Select, \
    SelectMultiple

from .models import  Author, Quote, Tag





class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']
        widgets = {
            'fullname': TextInput(attrs={'class': 'form-control'}),
            'born_date': DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'born_location': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'rows': 4, 'class': 'form-control'}),
        }


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
        }


class QuoteForm(ModelForm):
    class Meta:
        model = Quote
        fields = ['text', 'author', 'tags']
        widgets = {
            'text': Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'author': Select(attrs={'class': 'form-control'}),
            'tags': SelectMultiple(attrs={'class': 'form-control'})
        }
