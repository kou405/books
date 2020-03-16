from django.http import HttpResponse
from django.template import loader
from .models import Book, Report



def list_books(request):
    #books = Book.objects.filter(author='村上春樹')
    books = Book.objects.all()
    context = {
        'title': '本のリスト',
        'books': books,
    }
    template = loader.get_template('books/list_books.html')
    return HttpResponse(template.render(context, request))

def author_books(request, author):
    books = Book.objects.filter(author=author)
    context = {
        'title': '本のリスト',
        'books': books,
    }
    template = loader.get_template('books/list_books.html')
    return HttpResponse(template.render(context, request))


def detail_book(request, book_id):
    try:
        book = Book.objects.get(book_id=book_id)
    except Book.DoesNotExist:
        book = None

    context = {
        'title': '本の詳細',
        'book': book,
    }
    template = loader.get_template('books/detail_book.html')
    return HttpResponse(template.render(context, request))

def edit_book_input(request, book_id):
    try:
        book = Book.objects.get(book_id=book_id)
    except Book.DoesNotExist:
        book = None

    context = {
        'title': 'リストの編集(input)',
        'mode': 'input',
        'book': book,
    }
    template = loader.get_template('books/edit_book.html')
    return HttpResponse(template.render(context, request))

def edit_book_confirm(request, book_id):
    book = Book()
    book.book_id = request.POST['book_id']
    book.title = request.POST['title']
    book.author = request.POST['author']
    book.comment = request.POST['comment']

    context = {
        'title': 'リストの編集(confirm)',
        'mode': 'confirm',
        'warning_message': 'Are you sure you want to save?',
        'book': book,
    }
    template = loader.get_template('books/edit_book.html')
    return HttpResponse(template.render(context, request))

def edit_book_result(request, book_id):
    try:
        book = Book.objects.get(book_id=book_id)
        book.book_id = request.POST['book_id']
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.comment = request.POST['comment']
        book.save()
    except Book.DoesNotExist:
        book = None

    context = {
        'title': 'リストの編集(result)',
        'mode': 'result',
        'success_message': 'Success!',
        'book': book,
    }
    template = loader.get_template('books/edit_book.html')
    return HttpResponse(template.render(context, request))

def edit_book(request, book_id):
    if request.method == 'GET':
        return edit_book_input(request, book_id)
    elif request.method == 'POST':
        if request.POST['mode'] == 'input':
            return edit_book_confirm(request, book_id)
        if request.POST['mode'] == 'confirm':
            return edit_book_result(request, book_id)
