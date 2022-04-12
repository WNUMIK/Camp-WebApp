from django.contrib import admin

from . import models


@admin.register(models.Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


class TypeInline(admin.StackedInline):
    model = models.Type


@admin.register(models.Camping)
class CampingAdmin(admin.ModelAdmin):
    list_display = ('name', 'place', 'created')
    list_filter = ('created', 'place')
    search_fields = ('name', 'overview')
    prepopulated_fields = {'slug': ('name',)}
    inlines = (TypeInline,)