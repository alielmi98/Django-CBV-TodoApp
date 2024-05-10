from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "country", "city", "image"]
    date_hierarchy = "created_date"
    list_filter = ("country",)
    search_fields = ["user"]
