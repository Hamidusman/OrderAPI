from django.db import models  
from django.contrib.auth.models import User

# Create your models here.
FOODS = [
    ('spaghetti', 'Spaghetti'),
    ('pepperoni_pizza', 'Pepperoni Pizza'),
    ('bread', 'Bread'),
    ('ofada_rice', 'Ofada Rice'),
    ('iguana_on_a_stick', 'Iguana On A Stick'),
]

DRINKS = [
    ('pepsi', 'Pepsi'),
    ('water', 'Water'),
    ('xander', 'Xander'),
    ('nuka_cola', 'Nuka Cola')
]

class Order(models.Model):  
    customer = models.ForeignKey('auth.User', related_name='orders', on_delete=models.CASCADE)
    food = models.CharField(choices=FOODS, max_length=50, null=True)
    food_quantity = models.IntegerField(default=0)
    drink = models.CharField(choices=DRINKS, max_length=50, null=True)
    drink_quantity = models.IntegerField(default=0)
    ordered_at = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)