from django.urls import path
from .views import book_helper, my_bookings

urlpatterns = [
    path('book/<int:helper_id>/', book_helper, name='book_helper'),
    path('my-bookings/', my_bookings, name='my_bookings'),
]