from django.contrib import admin
from .models import Item

# Amend admin portal view for db
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("meal", "status")
    list_filter = ("status",)
    search_fields = ("meal", "description")

# Create admin portal
admin.site.register(Item, MenuItemAdmin)
