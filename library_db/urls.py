from django.contrib.auth.views import LogoutView
from django.urls import path

from portfolio import settings
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('login', views.login_view, name='login'),
    path('signup', views.initial_signup_view, name='signup'),
    path('logout', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('library_admin_login', views.admin_login_view, name='library_admin_login'),
    path('library_admin_page', views.admin_page, name='library_admin_page'),
    path('addtional_info', views.additional_info, name='additional_info'),
    path('book_list', views.book_list, name='book_list'),
    path('book_detail/<book>', views.book_detail, name='book_detail'),
    path('make_librarian/<user>', views.make_librarian, name='make_librarian'),
    path('delete_librarian/<librarian>', views.delete_librarian, name='delete_librarian'),
    path('insert_book', views.insert_book, name='insert_book'),
    path('book_copies/<book>', views.book_copies, name='book_copies'),
    path('add_new_copy/<book>', views.add_new_copy, name='add_new_copy'),
    path('delete_copy/<book>/<copy>', views.delete_copy, name='delete_copy'),
    path('librarian_book_list', views.librarian_book_list, name='librarian_book_list'),
    path('checkout/<copy>', views.checkout, name='checkout'),
    path('checkin/<checked>', views.checkin, name='checkin'),
    path('history_list', views.history_list, name='history_list'),
    path('history_detail/<current>', views.history_detail, name='history_detail')
]
