from django.db import models
from django.views.generic import ListView
from .models import Book

# Create your views here.

class BookListView(ListView):
    model = Book
    template = 'book_list.html'