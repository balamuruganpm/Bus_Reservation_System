from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('findbus', views.findbus, name="findbus"),
    path('bookings', views.bookings, name="bookings"),
    path('list', views.list, name="list"),
    path('bookings', views.bookings, name="bookings"),
    path('booklist', views.booklist, name="booklist"),
    path('cancellings', views.cancellings, name="cancellings"),
    path('seebookings', views.seebookings, name="seebookings"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('success', views.success, name="success"),
    path('signout', views.signout, name="signout"),
    path('about', views.about, name="about"),
    path('service', views.service, name="service"),
    path('depart', views.depart, name="depart"),
    path('blog', views.blog, name="blog"),
]
