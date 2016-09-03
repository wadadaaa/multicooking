from django.contrib import admin
from django.conf import settings
from shop.models import (
    Product,
    Catalog,
    Testimonial,
)

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('admin_thumbnail', 'name', 'is_featured')
    list_filter = ('created_at', 'is_featured')

    def admin_thumbnail(self, obj):
        return '<img src="%s%s" alt="" height="50">' % (settings.MEDIA_URL, obj.image)
    admin_thumbnail.allow_tags = True


class CatalogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('admin_thumbnail', 'name')

    def admin_thumbnail(self, obj):
        return '<img src="%s%s" alt="" height="50">' % (settings.MEDIA_URL, obj.image)
    admin_thumbnail.allow_tags = True


class TestimonialAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('admin_thumbnail', 'name')

    def admin_thumbnail(self, obj):
        return '<img src="%s%s" alt="" height="50">' % (settings.MEDIA_URL, obj.image)
    admin_thumbnail.allow_tags = True

admin.site.register(Product, ProductAdmin)
admin.site.register(Catalog, CatalogAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
