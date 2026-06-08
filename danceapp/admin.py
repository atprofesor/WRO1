from django.contrib import admin
from .models import Dance


@admin.register(Dance)
class DanceAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'slug')
    search_fields = ('name', 'country', 'slug')
