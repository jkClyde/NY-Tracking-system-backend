from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'customer_name', 'laundry_id', 'date_added', 'kilo', 'price', 'status', 'is_ready', 'is_claimed']
        read_only_fields = ['id', 'laundry_id', 'date_added']  # These fields should not be modified externally
