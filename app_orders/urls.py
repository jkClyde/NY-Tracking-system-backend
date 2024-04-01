from django.urls import path
from .views import OrderListCreateAPIView, ToggleClaimedStatus, ToggleReadyStatus, SearchOrder

urlpatterns = [
    path('orders/', OrderListCreateAPIView.as_view(), name='order-list-create'),
    path('toggle_ready_status/', ToggleReadyStatus.as_view(), name='toggle_ready_status'),
    path('toggle_claimed_status/', ToggleClaimedStatus.as_view(), name='toggle_claimed_status'),
    path('search/', SearchOrder.as_view(), name='search'),
]
