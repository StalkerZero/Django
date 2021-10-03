from django.contrib import admin

from .models import *

admin.site.register(Firm)
admin.site.register(Product)
admin.site.register(Buyer)
admin.site.register(Sold)

