from django.db import models

class Transaction(models.Model):
    stock_symbol = models.CharField(max_length=10)
    price_per_share = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_shares = models.IntegerField()
    transaction_date = models.DateField()
    broker_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.stock_symbol} - {self.transaction_date}"
