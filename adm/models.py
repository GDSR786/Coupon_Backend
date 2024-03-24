from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Store(models.Model):
    Name = models.CharField(max_length=255)

    def __str__(self):
        return self.Name


class Coupon(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.TextField(max_length=500)
    Code = models.CharField(max_length=255)
    Value = models.IntegerField()
    Store = models.ForeignKey(Store, on_delete=models.CASCADE)
    IsActive = models.BooleanField(default=True)
    Qty = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.Name


class Coupon_used(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.TextField(max_length=500)
    Code = models.CharField(max_length=255)
    Value = models.IntegerField()
    Store = models.CharField(max_length=255, blank=True, null=True)
    Usedby = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    Useddate = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)

    Remarks = models.TextField(max_length=500, blank=True, null=True)
    Amount_Taken = models.IntegerField(blank=True, null=True)
    Qty = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.Name
