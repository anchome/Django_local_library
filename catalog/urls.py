from django.urls import path
from django.contrib.auth import views as auth_views
from .import views


urlpatterns = [
    path('', views.index, name='index'), # abre página index.html
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('genres/', views.GenreListView.as_view(), name='genres'),
    path('genre/<int:pk>', views.GenreDetailView.as_view(),
         name='genre-detail'),
    path('languages/', views.LanguageListView.as_view(), name='languages'),
    path('languages/<int:pk>', views.LanguageDetailView.as_view(), name='language-detail')

]

urlpatterns += [
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('borrowed/', views.LoanedBooksAllListView.as_view(), name='all-borrowed')
]

#Añadir URLConf para que el bibliotecario renueve un libro.

urlpatterns += [
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]

# URLs author: crear, actualizar y borrar
urlpatterns += [
    path('author/create/', views.AuthorCreate.as_view(), name="author-create"),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name="author-update"),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name="author-delete"),
]

# URLs book: crear, actualizar y borrar

urlpatterns += [
    path('book/create/', views.BookCreate.as_view(), name="book-create"),
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name="book-update"),
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name="book-delete")
]

# URLs genre: crear, actualizar y borrar

urlpatterns += [
    path('genre/create/', views.GenreCreate.as_view(), name="genre-create"),
    path('genre/<int:pk>/update/', views.GenreUpdate.as_view(), name='genre-update'),
    path('genre/<int:pk>/delete/', views.GenreDelete.as_view(), name='genre-delete')
]

# URLs language: crear, actualizar y borrar

urlpatterns += [
    path('language/create/', views.LanguageCreate.as_view(), name="language-create"),
    path('language/<int:pk>/update/', views.LanguageUpdate.as_view(), name='language-update'),
    path('language/<int:pk>/delete/', views.LanguageDelete.as_view(), name='language-delete')
    
]


