from django.contrib import admin
from .models import Book
# Register your models here.

# admin.site.register(Book)

class PublishBook(admin.ModelAdmin):

    list_display = ('book_title', 'book_pages_num', 'book_category' , 'book_status' , 'book_date_of_publish')
    actions = ['Published', ]

    def Published(self, request, queryset):
        queryset.update(book_status="Published")
    
    Published.short_description = "Mark selected books as published"



admin.site.register(Book, PublishBook)