from django.db import models
from django.contrib.auth.models import User


class Firm(User):
    firm_name = models.CharField('Название', max_length=45)
    address = models.CharField('Адрес', max_length=100)
    last_name = models.CharField('Фамилия директора', max_length=45)
    phone_number = models.BigIntegerField('Телефон фирмы')

    def __int__(self):
        return self.id


class Buyer(User):
    phone_number = models.BigIntegerField('Телефон')
    buyer_type = models.CharField('Тип покупателя', max_length=45)

    def __int__(self):
        return self.id


class Product(models.Model):
    id_firm = models.ForeignKey(Firm, on_delete=True)
    title = models.CharField('Название', max_length=45)
    sort = models.CharField('Сорт', max_length=45)
    price = models.FloatField('Установленная цена')
    quantity = models.IntegerField('Количество')

    def __int__(self):
        return self.id


class Sold(models.Model):
    id_product = models.ForeignKey(Product, on_delete=True)
    id_buyer = models.ForeignKey(Buyer, on_delete=True)
    quantity = models.IntegerField('Количество проданных')
    buyer_type = models.ForeignKey(Buyer.buyer_type, on_delete=True)

    def __int__(self):
        return self.id
