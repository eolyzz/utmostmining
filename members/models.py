from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Members(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    account_type = models.CharField(max_length=255)
    account_status = models.CharField(max_length=255)
    wallet_balance = models.FloatField()
    invested = models.FloatField()
    total_withdrawal = models.FloatField()
    referral_bonus = models.FloatField()

    def __str__(self):
        return self.name
