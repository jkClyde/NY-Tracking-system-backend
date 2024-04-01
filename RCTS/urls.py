
from django.urls import path, include
from django.urls import path

urlpatterns = [
    path('orders/', include('app_orders.urls')),

]
