from django.contrib import admin
from .models import LibraryUser, Librarian, Book, BookCopy, Checkout, History, LibraryAdmin

# Register your models here.
admin.site.register(LibraryUser)
admin.site.register(Librarian)
admin.site.register(Book)
admin.site.register(BookCopy)
admin.site.register(Checkout)
admin.site.register(History)
admin.site.register(LibraryAdmin)