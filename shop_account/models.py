from django.db import models
from django.utils import timezone
'''
from user_account.models import UserAccount


class ShopModel(models.Model):

    id = models.AutoField(primary_key=True)
    shop_name = models.CharField(max_length=30)
    email = models.EmailField()

    total_employees = models.PositiveBigIntegerField()
    location = models.CharField(max_length=30)
    type_of_shop = models.CharField(max_length=30)
    phone = models.CharField(max_length=9)
    description = models.CharField(max_length=50)
    date_posted = models.DateTimeField(default=timezone.now)

    user_account = models.OneToOneField(UserAccount, on_delete=models.CASCADE)

    def __str__(self):
        return self.shop_name
'''