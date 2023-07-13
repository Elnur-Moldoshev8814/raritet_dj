from django.contrib import admin
from .models import Book, Filial, Author

admin.site.register(Filial)
admin.site.register(Book)
admin.site.register(Author)