from django.shortcuts import render, redirect, get_object_or_404
from bookings.models import Booking
from .models import Payment
from django.contrib.auth.decorators import login_required

# Create your views here.

@ login_required
def make_payment(request, booking_id):

    booking = get_object_or_404(Booking, id=booking_id)
    
    amount = booking.helper.price_per_day

    if request.method == "POST":
        payment_method = request.POST['payment_method']

        Payment.objects.create(
            user = request.user,
            booking = booking,
            amount =amount,
            payment_method = payment_method,
            payment_status = 'completed'
        )

        booking.status = 'confirmed'
        booking.save()

        return redirect('payment_success')
    
    return render(request, 'payment.html',{'booking':booking, 'amount':amount})

def payment_success(request):
    return render(request, 'payment_success.html')
