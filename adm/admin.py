from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Store)


class Coupon_Admin(admin.ModelAdmin):
    list_display = ('Name', 'Qty', 'Value', 'Amount_Taken', 'Store', 'Usedby', 'Useddate',)
    list_filter = ('Usedby', 'Useddate')


class Org_Admin(admin.ModelAdmin):
    list_display = ('Name', 'Qty', 'IsActive')


admin.site.register(Coupon, Org_Admin)
admin.site.register(Coupon_used, Coupon_Admin)
