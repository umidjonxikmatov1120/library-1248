from django.urls import path

from books.views import BookListView, BookCreateView, BookUpdateView, BookDetailView, BookDeleteView, AuthorListView, \
    AuthorCreateView, AuthorUpdateView, AuthorDetailView, AuthorDeleteView, BookListCreateView, \
    BookRetrieveUpdateDeleteView

urlpatterns = [
    path('', BookListView.as_view()),
    path('create/', BookCreateView.as_view()),
    path('update/<int:pk>/', BookUpdateView.as_view()),
    path('<int:pk>/', BookDetailView.as_view()),
    path('delete/<int:pk>/', BookDeleteView.as_view()),
    path('listcreate/', BookListCreateView.as_view()),
    path('booksingle/<int:pk>/', BookRetrieveUpdateDeleteView.as_view()),
    path('author', AuthorListView.as_view()),
    path('author/create', AuthorCreateView.as_view()),
    path('author/update/<int:pk>/', AuthorUpdateView.as_view()),
    path('author/<int:pk>/', AuthorDetailView.as_view()),
    path('author/delete/<int:pk>/', AuthorDeleteView.as_view()),
]