from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
# Register your models here.

from .models import Category, Banner


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title',)
    list_display_links = ('indented_title', )


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['admin_image', 'title', 'image', 'category', 'active']
    list_filter = ['active', 'category', ]
    readonly_fields = ['admin_image', ]