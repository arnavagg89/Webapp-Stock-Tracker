from django.shortcuts import render
from django.http import HttpResponse
from .models import Transaction
from .serializer import TransactionsSerializers
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def get_transactions(request):
    transactions = Transaction.objects.all()
    # return Response(transactions)
    return render(request, 'transactions.html', {'transactions': transactions})


# @api_view(['POST'])
def create_stock_transaction(request):
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return render(request, 'create_transaction.html')