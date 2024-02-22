from django.contrib import admin
from .models import Client, Product, Order

class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone_number')  # Отображаемые поля в списке объектов
    list_filter = ('name', 'email')  # Фильтрация по указанным полям
    search_fields = ('name', 'email', 'phone_number')  # Поля для поиска
    ordering = ('id',)  # Поля, по которым сортируются объекты

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'quantity')  # Отображаемые поля в списке объектов
    list_filter = ('name', 'price', 'quantity')  # Фильтрация по указанным полям
    search_fields = ('name',)  # Поля для поиска
    ordering = ('id',)  # Поля, по которым сортируются объекты

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'total_amount', 'order_date')  # Отображаемые поля в списке объектов
    list_filter = ('client', 'order_date')  # Фильтрация по указанным полям
    search_fields = ('client__name',)  # Поля для поиска (можно использовать связанные поля)
    ordering = ('id',)  # Поля, по которым сортируются объекты

admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)