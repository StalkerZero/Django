from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Firm, Buyer
from phonenumber_field.formfields import PhoneNumberField


class FirmCreate(UserCreationForm):
    address = forms.CharField(label="Адрес", max_length=150)
    phone_number = PhoneNumberField(label='Телефон', region="RU")

    class Meta:
        model = Firm
        fields = ('username', 'password1', 'password2', 'address', 'last_name', 'phone_number')
