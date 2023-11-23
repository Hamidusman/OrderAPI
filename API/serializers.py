from rest_framework import serializers
from .models import Order, FOODS, DRINKS
from django.contrib.auth.models import User

class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.ReadOnlyField(source='customer.username')

    class Meta:
        model = Order
        fields = ['customer', 'food', 'food_quantity', 'drink', 'drink_quantity', 'ordered_at', 'completed']

class UserSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'orders']

    # If you want to allow creating orders through the user endpoint
    def create(self, validated_data):
        orders_data = validated_data.pop('order', None)

        user = User.objects.create(**validated_data)

        if orders_data:
            for order_data in orders_data:
                Order.objects.create(user=user, **order_data)

        return user