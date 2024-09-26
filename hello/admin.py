from django.contrib import admin
from hello.models import User, UsersDog, Order

admin.site.register(User)
admin.site.register(UsersDog)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['dog', 'name', 'phone', 'date']
