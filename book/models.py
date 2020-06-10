from django.db import models
from django.contrib.auth.models import User # can be removed
from django.utils import timezone
from author.models import Author
# Create your models here.

BOOK_STATUS_CHOICES = (
        ('Published','Published'), 
        ('Withdrawn','Withdrawn'), 
        ('Draft','Draft'),
    )

class Book(models.Model):
    book_author = models.ForeignKey(Author, on_delete = models.CASCADE , related_name='AuthorBooks')
    book_title = models.CharField(max_length=50)
    book_category = models.CharField(max_length=20)
    book_pages_num = models.IntegerField()
    book_date_of_publish = models.DateTimeField(default=timezone.now)
    book_status = models.CharField( 
        max_length = 20, 
        choices = BOOK_STATUS_CHOICES, 
        default = 'Published'
        )
    


    def __str__(self):
        return self.book_title

   