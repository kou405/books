from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_books, name='list_books'),
    path('author/<str:author>/', views.author_books, name='author_books'),
    path('detail/<str:book_id>/', views.detail_book, name='detail_book'),
    path('detail/<str:book_id>/edit', views.edit_book, name='edit_book'),
]
