from django.db import models

# Create your models here.
class Author(models.Model):  
    full_name = models.TextField()  
    birth_year = models.SmallIntegerField()  
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name

class Book(models.Model):  
    ISBN = models.CharField(max_length=13)  
    title = models.TextField()  
    description = models.TextField()  
    year_release = models.SmallIntegerField()  
    copy_count = models.SmallIntegerField(default=1)
    price = models.DecimalField(default=None, max_digits=12, decimal_places=2)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    redaction = models.ForeignKey('Redaction', on_delete=models.CASCADE, null=True, blank=True, related_name='books')

    def __str__(self):
    	return self.title


class Redaction(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self):
        return self.name