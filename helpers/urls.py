from django.urls import path
from .views import add_helper, helper_list, delete_helper, update_helper

urlpatterns = [
    path('add/', add_helper, name='add_helpers' ),
    path('', helper_list, name="helper_list"),
    path('delete/<int:id>/', delete_helper, name='delete_helper'),
    path('update/<int:id>/', update_helper, name='update_helper'),
]