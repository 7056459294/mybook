from django.contrib import admin

# Register your models here.
from .models import books,Contact,users,soldbooks

admin.site.register(books)
admin.site.register(Contact)
admin.site.register(users)
admin.site.register(soldbooks)