from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookingForm
from helpers.models import Helper
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def book_helper(request, helper_id):
    helper = get_object_or_404(Helper, id=helper_id)
    form =BookingForm(request.POST or None)
    
    if form.is_valid():
        booking = form.save(commit=False)
        booking.user = request.user
        booking.helper = helper
        booking.save()
        return redirect('my_bookings')

    return render (request, 'booking_helper.html', {'form':form,'helper':helper})

@login_required
def my_bookings(request):
    bookings = request.user.booking_set.all()
    return render (request, 'my_bookings.html', {'bookings': bookings})