from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Firm(User):
    address = models.CharField(max_length=100)
    # last_name = models.CharField('Фамилия директора', max_length=45)
    phone_number = PhoneNumberField(region="RU")

    def __int__(self):
        return self.id


class Buyer(User):
    phone_number = PhoneNumberField(region="RU", null=True)
    buyer_type = models.CharField(max_length=45)

    def __int__(self):
        return self.id


class Product(models.Model):
    id_firm = models.ForeignKey(Firm, on_delete=models.CASCADE)
    title = models.CharField(name='Название', max_length=45)
    sort = models.CharField(name='Сорт', max_length=45)
    price = models.FloatField(name='Цена')
    quantity = models.IntegerField(name='Количество')

    def __int__(self):
        return self.id


class Sold(models.Model):
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    id_buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    quantity = models.IntegerField(name='Кол-во проданных изделий')
    buyer_type = models.CharField(name='Тип покупателя', max_length=45)

    def __int__(self):
        return self.id
