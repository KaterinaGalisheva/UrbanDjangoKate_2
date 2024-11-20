from django.contrib import admin
from .models import Buyer, Game

# Register your models here.

from django.contrib import admin
from .models import Buyer, Game

# Админка для модели Buyer
@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    # Поля для отображения в списке
    list_display = ('name', 'balance', 'age', 'purchased_games')
    # Поля для поиска
    search_fields = ('id', 'name')
    # Фильтры
    list_filter = ('age',)
    # Сортировка
    ordering = ('id',)
    # Форма для редактирования
    fieldsets = (
        (None, {
            'fields': ('name', 'balance', 'age')
        }),
    )


# Админка для модели Game
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    # Поля для отображения в списке
    list_display = ('title', 'cost', 'size', 'age_limited', 'buyer_count')
    # Поля для поиска
    search_fields = ('title', 'cost', 'age_limited')
    # Фильтры
    list_filter = ('age_limited',)
    # Сортировка
    ordering = ('title',)
    # Форма для редактирования
    fieldsets = (
        (None, {
            'fields': ('title', 'cost', 'size', 'description', 'age_limited', 'buyer')
        }),
    )

    # Отображение количества покупателей в списке игр
    def buyer_count(self, obj):
        return obj.buyer.count()
    buyer_count.short_description = 'Количество покупателей'

    