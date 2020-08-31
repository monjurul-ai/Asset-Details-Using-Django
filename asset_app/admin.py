from django.contrib import admin

# Register your models here.
from asset_app.models import Laptop, Desktop

admin.site.register(Laptop)
admin.site.register(Desktop)
