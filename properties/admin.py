from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag

    
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    model = Property

    list_display = (
        "id",
        "owner",
        "city",
        "neighborhood",
        "street",
        "slug",
        "short_description",
        "publish_date",
        "published",
    )
    list_filter = (
        "city",
        "neighborhood",
        "published",
        "publish_date",
    )
    list_editable = (
        "city",
        "street",
        "short_description",
        "slug",
        "publish_date",
        "published",
    )
    search_fields = (
        "city",
        "short_description",
        "slug",
        "description",
    )
    prepopulated_fields = {
        "slug": (
            "city",
            "neighborhood",
        )
    }
    date_hierarchy = "publish_date"
    save_on_top = True