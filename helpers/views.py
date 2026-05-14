
from django.shortcuts import render,redirect, get_object_or_404
from .models import Helper
from .forms import HelperForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def add_helper(request):
    form = HelperForm(request.POST or None , request.FILES or None)

    if form.is_valid():
        helper = form.save(commit=False)
        helper.user = request.user
        helper.save()
        return redirect('helper_list')
    return render(request, 'add_helper.html', {'form':form})
    
def helper_list(request):
    
    service = request.GET.get('service')

    if service:

        helpers = Helper.objects.filter(
            skills__icontains=service
        )

    else:


        helpers =Helper.objects.all()
    return render(request, 'helper_list.html', {'helpers': helpers})

def delete_helper(request, id):
    helper = get_object_or_404(Helper, id)

    if helper.user == request.user:
        helper.delete()

    return redirect('helper_list')

@login_required
def update_helper(request, id):
    helper = get_object_or_404(Helper, id=id)

    if helper.user != request.user:
        return redirect('helper_list')

    form = HelperForm(request.POST or None, request.FILES or None, instance=helper)

    if form.is_valid():
        form.save()
        return redirect('helper_list')

    return render(request, 'add_helper.html', {'form': form})