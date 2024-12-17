from django.contrib import admin
from .models import Gullar, Turlar
@admin.register(Gullar)
class GullarAdmin(admin.ModelAdmin):
    list_display = ('nom', 'tavsif', 'turlar')
    search_fields = ('nom',)
@admin.register(Turlar)
class TurlarAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ('nom',)

