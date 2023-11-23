
from .serializers import OrderSerializer, UserSerializer
from .permissions import CustomerOrReadOnly
from rest_framework import permissions
from .models import Order
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import mixins
# Create your views here.


class orders(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class =OrderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
         serializer.save(customer=self.request.user)
        
class order_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, CustomerOrReadOnly]
 

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer