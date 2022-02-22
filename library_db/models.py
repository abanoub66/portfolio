from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class LibraryUser(models.Model):
    STATUS_TYPES = (
        ('excellent', 'excellent'),
        ('good', 'good'),
        ('probationary', 'probationary'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthdate = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_TYPES, default='good')

    def __str__(self):
        return self.user.username


class Librarian(models.Model):
    librarian_id = models.ForeignKey(LibraryUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.librarian_id.user.username


class LibraryAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    publish_date = models.DateField()
    number_of_pages = models.IntegerField()

    def __str__(self):
        return self.title + ' written by ' + self.author

    class Meta:
        unique_together = (('title', 'author'),)


class BookCopy(models.Model):
    book_key = models.ForeignKey(Book, on_delete=models.CASCADE)
    copy_number = models.IntegerField()
    book_in = models.BooleanField(default=True)

    def __str__(self):
        if self.book_in:
            return str(self.book_key) + ' copy ' + str(self.copy_number) + ' is in'
        else:
            return str(self.book_key) + ' copy ' + str(self.copy_number) + ' is out'

    class Meta:
        unique_together = (('book_key', 'copy_number'),)


class Checkout(models.Model):
    user_id = models.ForeignKey(LibraryUser, on_delete=models.DO_NOTHING)
    librarian_id = models.ForeignKey(Librarian, on_delete=models.DO_NOTHING)
    book_copy = models.ForeignKey(BookCopy, on_delete=models.DO_NOTHING)
    date_of_checkout = models.DateTimeField()
    due_date = models.DateField()

    def __str__(self):
        return str(self.user_id) + ' checked out ' + str(self.book_copy) + ' with ' + str(self.librarian_id) + ' on ' + \
               str(self.date_of_checkout) + ' and it is due on ' + str(self.due_date)


class History(models.Model):
    checkout = models.OneToOneField(Checkout, on_delete=models.DO_NOTHING)
    date_of_checkin = models.DateTimeField(default=None, blank=True, null=True)

    def __str__(self):
        if self.date_of_checkin is not None:
            return str(self.checkout) + ' and was returned on ' + str(self.date_of_checkin)
        else:
            return str(self.checkout)
