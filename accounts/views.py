from django.shortcuts import render,redirect
from .forms  import SignupForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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
    
    return render(request, 'user_dashboard.html')