from django.shortcuts import render
from p_library.models import Author, Book, Redaction
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader

def books_list(request):
    books = Book.objects.all()
    return HttpResponse(books)
def index(request):
    template = loader.get_template('index.html')
    books = Book.objects.all()
    biblio_data = {
        "title": "мою библиотеку",
        "books": books,
        "val": range(1,101,1),
    }
    return HttpResponse(template.render(biblio_data, request))

def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            book.copy_count += 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')

def redactions(request):
    template = loader.get_template('redactions.html')
    redactions = Redaction.objects.all()
    data = {
        "redactions": redactions,
    }
    return HttpResponse(template.render(data, request))