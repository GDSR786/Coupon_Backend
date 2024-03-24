# Generated by Django 5.0.3 on 2024-03-23 13:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='Amount_Taken',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='Remarks',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='Usedby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='Useddate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
