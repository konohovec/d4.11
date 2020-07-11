from django.contrib import admin
from django.urls import path
from p_library import views
from p_library.views import BookEdit, AuthorEdit, AuthorList,  author_create_many,  books_authors_create_many, FriendList, FriendUpdate,FriendEdit, BookDetailView
app_name = 'p_library'  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.books_list),
    path('index/', views.index),
    path('index/book_increment/', views.book_increment),
    path('index/book_decrement/', views.book_decrement),
    path('redactions/', views.redactions),
    path('book/create', BookEdit.as_view(), name='book_create'),
    path('author/create', AuthorEdit.as_view(), name='author_create'),  
  	path('authors', AuthorList.as_view(), name='author_list'),  
  	path('author/create_many', author_create_many, name='author_create_many'),  
  	path('author_book/create_many', books_authors_create_many, name='author_book_create_many'),
    path('friends', FriendList.as_view(), name='friend_list'),
    path('<pk>/friend_update', FriendUpdate.as_view(), name='friend_update'),
    path('friend/create', FriendEdit.as_view(), name='friend_create'),
    path('book/<int:pk>', BookDetailView.as_view(), name='book_detail')

]
