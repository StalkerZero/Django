# Generated by Django 3.2.7 on 2021-10-03 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_sold_buyer_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyer',
            name='purchased_products',
        ),
    ]
