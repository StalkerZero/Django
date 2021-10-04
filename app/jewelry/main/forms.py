from django import forms
from django.contrib.auth.forms import *
from django.contrib.auth.models import User
from django.forms import BaseForm
from django.utils.translation import gettext_lazy as _

from .models import Firm, Buyer, Product


class FirmCreate(UserCreationForm):
    username = UsernameField(label="Название фирмы",
                             localize="ru",
                             max_length=150,
                             help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
                             validators=[User.username_validator],
                             error_messages={
                                 'unique': _("A user with that username already exists."),
                             }, )

    last_name = forms.CharField(label="Фамилия директора", max_length=150)

    class Meta:
        model = Firm
        fields = ('username', 'password1', 'password2', 'address', 'last_name', 'phone_number')


class BuyerCreate(UserCreationForm):
    class Meta:
        model = Buyer
        fields = ('username', 'password1', 'password2', 'phone_number', 'buyer_type')


class TestForm(forms.ModelForm):

    class Meta:
        model = Product
        quantity = forms.IntegerField(label='Сколько')
        id = forms.IntegerField
        fields = ('quantity', 'id')


# class BuyerUpdate(UserChangeForm):
#     # password = forms.PasswordInput(_('password'))
#
#     class Meta:
#         model = Buyer
#         fields = ('username', 'phone_number', 'buyer_type')

# class ProductForm(forms.Form):
#     model = Product
#     fields = ('title', 'sort', 'price', 'quantity')
