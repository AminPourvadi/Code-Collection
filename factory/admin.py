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
    NavigationLink,
    Steel
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
    list_display = ('title_en', 'title_fa', 'title_ar', 'image')

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title','description')


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('address_en', 'address_fa', 'address_ar', 'phone', 'email')
    search_fields = ('address_en', 'address_fa', 'address_ar', 'phone', 'email')


@admin.register(Steel)
class SteelAdmin(admin.ModelAdmin):
    list_display = ('title_en', 'title_fa', 'title_ar', 'description1_en', 'description1_fa', 'description1_ar', 'image')
    search_fields = ('title_en', 'title_fa', 'title_ar')
    list_filter = ('title_en', 'title_fa', 'title_ar')
    ordering = ('-id',)



class NavigationLinkAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'file', 'order', 'is_active', 'language']
    list_filter = ['is_active', 'language']
    search_fields = ['title', 'url']
    ordering = ['order']

admin.site.register(NavigationLink, NavigationLinkAdmin)


class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')  
    search_fields = ('question',)  
    list_filter = ('question',) 

admin.site.register(FAQ, FAQAdmin)

from django.contrib import admin
from .models import FooterInfo

@admin.register(FooterInfo)
class FooterInfoAdmin(admin.ModelAdmin):
    list_display = ('about_text', 'address', 'phone', 'email', 'copyright_text')

    