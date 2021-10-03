from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Firm(User):
    address = models.CharField(verbose_name='Адрес', max_length=100)
    phone_number = PhoneNumberField(verbose_name='Телефон фирмы', region="RU")

    def __int__(self):
        return self.id


class Product(models.Model):
    id_firm = models.ForeignKey(Firm, on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Название', max_length=45)
    sort = models.CharField(verbose_name='Сорт', max_length=45)
    price = models.FloatField(verbose_name='Цена')
    quantity = models.IntegerField(verbose_name='Количество')

    def __int__(self):
        return self.id


class Buyer(User):
    phone_number = PhoneNumberField(verbose_name='Номер телефона', region="RU", null=True)
    buyer_type = models.IntegerField(verbose_name='Тип покупателя', choices=[(1, 'Частный'), (2, 'Юр. Лицо')])

    def __int__(self):
        return self.id


class Sold(models.Model):
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    id_buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='Кол-во проданных изделий')
    buyer_type = models.CharField(verbose_name='Тип покупателя', max_length=11)

    def __int__(self):
        return self.id
