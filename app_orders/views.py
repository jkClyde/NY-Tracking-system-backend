from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from .serializers import OrderSerializer


class OrderListCreateAPIView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ToggleReadyStatus(APIView):
    def post(self, request, format=None):
        try:
            order_id = request.data.get('order_id')
            is_ready = request.data.get('is_ready')

            order = Order.objects.get(id=order_id)
            order.is_ready = is_ready
            order.save()

            serializer = OrderSerializer(order)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ToggleClaimedStatus(APIView):
    def post(self, request, format=None):
        try:
            order_id = request.data.get('order_id')
            is_claimed = request.data.get('is_claimed')

            order = Order.objects.get(id=order_id)
            order.is_claimed = is_claimed
            order.save()

            serializer = OrderSerializer(order)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class SearchOrder(APIView):
    def post(self, request, format=None):
        try:
            search_query = request.data.get('laundry_id')  # Update to retrieve 'laundry_id'
            if search_query is None:
                raise ValueError("No 'laundry_id' provided")

            orders = Order.objects.filter(laundry_id=search_query)  # Filter by 'laundry_id'
            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
