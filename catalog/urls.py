from django.conf.urls import url
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += [
    # Books List and Detail views
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
]

urlpatterns += [
    # Author List and Detaol views
    url(r'^authors/$', views.AuthorListView.as_view(), name='author'),
    url(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
]

urlpatterns += [
    #Add Django site authentication urls (for login, logout, password management)
    url(r'^accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += [
    url(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
url(r'^borrowed_books/$', views.LoanedBooksByUsersListViewForLibrarians.as_view(), name='all-borrowed'),
]