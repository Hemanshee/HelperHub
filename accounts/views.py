from django.shortcuts import render,redirect
from .forms  import SignupForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from bookings.models import Booking
from helpers.models import Helper

# Create your views here.
# signup view
def signup_view(request):
    form = SignupForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return redirect('login')
    return render(request,'signup.html',{'form':form})

# login view
def login_view(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)

        if user:
            login(request,user)
            return redirect('dashboard')
        
    return render(request, 'login.html')

# logout view
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    user = request.user

    if user.user_type == 'helper':
        return render(request,'helper_dashboard.html')
    
    total_bookings = Booking.objects.filter(
        user=request.user
    ).count()

    pending_count = Booking.objects.filter(
        user=request.user,
        status='pending'
    ).count()

    confirmed_count = Booking.objects.filter(
        user=request.user,
        status='confirmed'
    ).count()

    total_helpers = Helper.objects.count()

    recent_bookings = Booking.objects.filter(
        user=request.user
    ).order_by('-id')[:3]

    context = {

        'total_bookings': total_bookings,

        'pending_count': pending_count,

        'confirmed_count': confirmed_count,

        'total_helpers': total_helpers,

        'recent_bookings': recent_bookings

    }


    return render(request, 'user_dashboard.html')