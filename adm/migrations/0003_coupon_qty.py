# Generated by Django 5.0.3 on 2024-03-24 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0002_alter_coupon_amount_taken_alter_coupon_remarks_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='Qty',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]