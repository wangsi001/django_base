from django.contrib import admin

from book.models import Book,Person
# Register your models here.
admin.site.register(Book)
admin.site.register(Person)