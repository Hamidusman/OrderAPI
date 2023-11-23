from rest_framework import serializers
from .models import Order, FOODS, DRINKS
from django.contrib.auth.models import User

class OrderSerializer(serializers.ModelSerializer): 
    customer = serializers.ReadOnlyField(source='customer.username')
    class Meta:
        model = Order
        fields = ['customer', 'food', 'food_quantity', 'drink', 'drink_quantity', 'ordered_at', 'completed']

class UserSerializer(serializers.ModelSerializer):
    order = serializers.PrimaryKeyRelatedField(many=True, queryset=Order.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'order']
    
    def create(self, validated_data):
        # Extract the 'owner' data and remove it from the validated_data
        owner_data = validated_data.pop('owner', None)
        
        # Create the Order instance
        order = Order.objects.create(**validated_data)

        # Set the 'owner' relationship separately
        if owner_data:
            order.customer = owner_data.get('customer', None)
            order.save()

        return order