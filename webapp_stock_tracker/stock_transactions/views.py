from django.shortcuts import render
from django.http import HttpResponse
from .models import Transaction

# Create your views here.

def home(request):
    transactions = Transaction.objects.all()
    return render(request, 'transactions.html', {'transactions': transactions})

def add_transaction(request):
    
    Transaction.objects.create()