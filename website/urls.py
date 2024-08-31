from django.urls import path
from . import views  # Import views from the current directory

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('customer/<int:pk>', views.customer_record, name='customer'),
    path('Delete_customer/<int:pk>', views.Delete_customer, name='Delete'),
    path('Add_customer', views.Add_customer, name='Add'),
    path('Update_customer/<int:pk>', views.Update_customer, name='Update'),
    # other paths...
]
 