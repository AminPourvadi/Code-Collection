from django.contrib import admin
from .models import (
    Company,
    Employee,
    Image,
    Slider,
    Article,
    CompanyInfo,
    Product,
    FAQ,
    Feature,
    ContactInfo,
)


# ثبت مدل‌ها در پنل ادمین
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'email', 'phone', 'website')
    search_fields = ('name', 'location', 'email')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'company')
    search_fields = ('name', 'role')
    list_filter = ('company',)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('company', 'description')
    list_filter = ('company',)


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    ordering = ('-created_at',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'summary')
    ordering = ('-created_at',)


@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    ordering = ('-created_at',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'dimensions')
    search_fields = ('title',)
    list_filter = ('price',)
    ordering = ('title',)


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question',)
    search_fields = ('question',)


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('office_address', 'phone_number', 'email')
    search_fields = ('office_address', 'phone_number', 'email')
