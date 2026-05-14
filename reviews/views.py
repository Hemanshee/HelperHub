from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
from helpers.models import Helper
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required

def add_review(request, helper_id):
    helper = get_object_or_404(Helper, id=helper_id)

    if  request.method == "POST" :
        rating = request.POST['rating']
        comment = request.POST['comment']

        Review.objects.create(

            user = request.user,
            helper =helper,
            rating = rating,
            comment = comment

        )

        helper.update_rating() # helpers/model.py se call

        return redirect('helper_list')
    
    return render (request, 'add_review.html', {'helper':helper})
