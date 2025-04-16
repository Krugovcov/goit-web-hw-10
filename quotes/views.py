from pathlib import Path

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.paginator import Paginator
from .forms import QuoteForm, AuthorForm, TagForm
from .models import Quote, Author


def index(request):
    quotes_list = Quote.objects.all()
    paginator = Paginator(quotes_list, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'quotes/index.html', {'page_obj': page_obj})
# Create your views here.
@login_required()
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quotes:home')
    else:
        form = QuoteForm()

    return render(request, 'quotes/add_quote.html', {'form': form})

@login_required()
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('quotes:home')
    else:
        form = AuthorForm()

    return render(request, 'quotes/add_author.html', {'form': form})
@login_required()
def add_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('quotes:home')
    else:
        form = TagForm()

    return render(request, 'quotes/add_tag.html', {'form': form})

def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'quotes/author_detail.html', {'author': author})