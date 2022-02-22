import datetime

from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from .models import LibraryAdmin, LibraryUser, Librarian, Book, BookCopy, Checkout, History
from . import forms


def book_list(request):
    books = Book.objects.all().order_by('author', 'title')
    return render(request, 'library_db/book_list.html', {'books': books})


def librarian_book_list(request):
    user = request.user
    librarians = Librarian.objects.all()
    users = LibraryUser.objects.exclude(librarian__in=librarians)
    if user not in users:
        books = Book.objects.all().order_by('author', 'title')
        return render(request, 'library_db/librarian_book_list.html', {'books': books})
    else:
        return redirect('library_db:login')


@login_required(login_url='library_db/login/')
def book_detail(request, book):
    book = list(book.split(" written by "))
    b = Book.objects.get(title=book[0], author=book[1])
    copies = BookCopy.objects.filter(book_key=b)
    user = LibraryUser.objects.get(user__username=request.user)
    #histories = History.objects.get(checkout__user_id=user, date_of_checkin=None)
    check_outs = Checkout.objects.filter(user_id=user, book_copy__book_in=False, history__date_of_checkin=None)
    return render(request, 'library_db/book_detail.html', {'copies': copies, 'book': b, 'out_copies': check_outs})


def insert_book(request):
    user = request.user
    librarians = Librarian.objects.all()
    users = LibraryUser.objects.exclude(librarian__in=librarians)
    if user not in users:
        if request.method == 'POST':
            form = forms.CreateBook(request.POST)
            if form.is_valid():
                book = form.save()
                return redirect('library_db:book_copies', book=book)
        else:
            form = forms.CreateBook()
            return render(request, 'library_db/book_creation.html', {'form': form})
    else:
        return redirect('library_db:login')


def initial_signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('library_db:additional_info')
    else:
        form = UserCreationForm()
    return render(request, 'library_db/signup.html', {'form': form})


def additional_info(request):
    if request.method == 'POST':
        birth_string = request.POST['birthdate']
        birth_list = birth_string.split('/')
        birthdate = datetime.date(int(birth_list[2]), int(birth_list[0]), int(birth_list[1]))
        try:
            form = LibraryUser.objects.create(user_id=request.user.id, user=request.user,
                                              first_name=request.POST['first_name'],
                                              last_name=request.POST['last_name'],
                                              birthdate=birthdate)
        except IntegrityError:
            form = forms.CreateLibraryUser()
            render(request, 'library_db/additional_info.html', {'form': form})
        form.save()
        return redirect('library_db:book_list')
    else:
        form = forms.CreateLibraryUser()
    return render(request, 'library_db/additional_info.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('library_db:book_list')
    else:
        form = AuthenticationForm()
    return render(request, 'library_db/login.html', {'form': form})


def admin_login_view(request):
    error_message = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            admin = LibraryAdmin.objects.get(username=username, password=password)
        except LibraryAdmin.DoesNotExist:
            admin = None
        if admin is not None:
            user = authenticate(request, username='admin', password='librariesarecool')
            login(request, user)
            return redirect('library_db:library_admin_page')
        else:
            error_message = 'Wrong username or password'
    return render(request, 'library_db/library_admin_login.html', {'error_message': error_message})


def admin_page(request):
    if request.user.username == 'admin':
        librarians = Librarian.objects.all()
        users = LibraryUser.objects.exclude(librarian__in=librarians)
        return render(request, 'library_db/library_admin_page.html', {'librarians': librarians, 'users': users})
    else:
        return redirect('library_db:library_admin_login')


def make_librarian(request, user):
    if request.method == 'POST':
        u = LibraryUser.objects.filter(user__username=user)
        Librarian.objects.create(librarian_id=u[0]).save()
    return redirect('library_db:library_admin_page')


def delete_librarian(request, librarian):
    if request.method == 'POST':
        l = LibraryUser.objects.filter(user__username=librarian)
        Librarian.objects.filter(librarian_id=l[0]).delete()
    return redirect('library_db:library_admin_page')


def book_copies(request, book):
    user = request.user
    librarians = Librarian.objects.all()
    users = LibraryUser.objects.exclude(librarian__in=librarians)
    if user not in users:
        book = list(book.split(" written by "))
        b = Book.objects.get(title=book[0], author=book[1])
        copies = BookCopy.objects.filter(book_key=b)
        return render(request, 'library_db/book_copies.html', {'copies': copies, 'book': b})
    else:
        return redirect('library_db:login')


def add_new_copy(request, book):
    if request.method == 'POST':
        book = list(book.split(" written by "))
        b = Book.objects.get(title=book[0], author=book[1])
        last = BookCopy.objects.filter(book_key=b).order_by('copy_number').last()
        if last is None:
            BookCopy.objects.create(book_key=b, copy_number=1).save()
        else:
            BookCopy.objects.create(book_key=b, copy_number=last.copy_number + 1).save()
    return redirect('library_db:book_copies', book=b)


def delete_copy(request, book, copy):
    if request.method == 'POST':
        book = list(book.split(" written by "))
        copy = list(copy.split(" copy "))
        b = Book.objects.get(title=book[0], author=book[1])
        BookCopy.objects.get(book_key=b, copy_number=copy[1][0]).delete()
    return redirect('library_db:book_copies', book=b)


def checkout(request, copy):
    user = LibraryUser.objects.get(user=request.user)
    number_of_weeks = datetime.timedelta(days=14)
    due_date = datetime.date.today() + number_of_weeks
    # get user status
    # good equals 2 weeks
    # excellent 4 weeks
    # probationary 1 week
    if request.method == 'POST':
        l = LibraryUser.objects.get(user__username=request.POST['librarian'])
        librarian = Librarian.objects.get(librarian_id=l)
        copy = list(copy.split(" copy "))
        copy_number = copy[1][0]
        b = list(copy[0].split(" written by "))
        book = Book.objects.get(title=b[0], author=b[1])
        c = BookCopy.objects.get(book_key=book, copy_number=copy_number)
        c.book_in = False
        c.save()
        ch = Checkout.objects.create(user_id=user, librarian_id=librarian, book_copy=c,
                                     date_of_checkout=datetime.datetime.now(), due_date=due_date)
        ch.save()
        History.objects.create(checkout=ch).save()
        return redirect('library_db:history_detail', current=ch)
    librarians = Librarian.objects.all()
    return render(request, 'library_db/checkout.html', {'librarians': librarians, 'copy': copy, 'due_date': due_date})


def checkin(request, checked):
    user = LibraryUser.objects.get(user__username=request.user)
    checked = list(checked.split(' copy '))
    date = checked[1]
    date = list(date.split(' and '))
    date_of_checkout = list(date[0].split(' on '))[1]
    due_date = list(date[1].split(' on '))[1]
    copy_number = checked[1][0]
    checked = list(checked[0].split(' out '))
    checked = list(checked[1].split(' written by '))
    title = checked[0]
    author = checked[1]
    book = Book.objects.get(title=title, author=author)
    copy = BookCopy.objects.get(book_key=book, copy_number=copy_number)
    ch = Checkout.objects.get(user_id=user, book_copy=copy, date_of_checkout=date_of_checkout, due_date=due_date,
                              book_copy__book_in=False)
    copy.book_in = True
    copy.save()
    check_in = History.objects.get(checkout=ch)
    check_in.date_of_checkin = datetime.datetime.now()
    check_in.save()
    return redirect('library_db:book_list')


def history_list(request):
    user = request.user
    librarians = Librarian.objects.all()
    users = LibraryUser.objects.exclude(librarian__in=librarians)
    if user not in users:
        histories = History.objects.all().order_by('checkout__date_of_checkout')
        return render(request, 'library_db/history_list.html', {'histories': histories})
    else:
        return redirect('library_db:login')


def history_detail(request, current):
    return render(request, 'library_db/history_detail.html', {'checkout': current})
