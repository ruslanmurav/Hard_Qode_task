from django.contrib import admin

# Register your models here.
from product.models import Access, Product


@admin.register(Access)
class AdminAccess(admin.ModelAdmin):
    pass

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    pass