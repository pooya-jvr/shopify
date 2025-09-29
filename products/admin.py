from django.contrib import admin
from .models import Product, Category, SubCategory, Cart, CartItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_active", "created_at")
    search_fields = ("name",)
    list_filter = ("is_active",)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "is_active", "created_at")
    search_fields = ("name",)
    list_filter = ("is_active", "category")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "category",
        "sub_category",
        "price",
        "discount",
        "stock",
        "sold",
        "created_at",
    )
    search_fields = ("name", "description")
    list_filter = ("category", "sub_category", "stock")
    autocomplete_fields = ("category", "sub_category", "created_by", "updated_by")


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0
    readonly_fields = ("product", "quantity", "total_price")
    can_delete = False

    def total_price(self, obj):
        return obj.total_price

    total_price.short_description = "Total Price"


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "created_at", "total_price")
    search_fields = ("user__username",)
    list_filter = ("created_at",)
    inlines = [CartItemInline]

    def total_price_display(self, obj):
        return obj.total_price

    total_price_display.short_description = "Total Price"


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("id", "cart", "product", "quantity", "total_price")
    search_fields = ("product__name", "cart__user__username")
