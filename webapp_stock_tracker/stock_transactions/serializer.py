from rest_framework import serializers
 
# import model from models.py
from .models import Transaction
 
# Create a model serializer
class TransactionsSerializers(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = Transaction
        fields = ('stock_symbol', 'price_per_share', 'number_of_shares','transaction_date','broker_fee')