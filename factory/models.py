from django.db import models
from django.utils.translation import gettext_lazy as _

class Company(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("نام شرکت"))
    description = models.TextField(verbose_name=_("توضیحات"))
    location = models.CharField(max_length=255, verbose_name=_("موقعیت"))
    email = models.EmailField(verbose_name=_("ایمیل"))
    phone = models.CharField(max_length=20, verbose_name=_("تلفن"))
    website = models.URLField(verbose_name=_("وبسایت"))

    def __str__(self):
        return self.name


class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="employees", verbose_name=_("شرکت"))
    name = models.CharField(max_length=100, verbose_name=_("نام"))
    role = models.CharField(max_length=100, verbose_name=_("نقش"))
    bio = models.TextField(verbose_name=_("بیوگرافی"))
    linkedin = models.URLField(blank=True, null=True, verbose_name=_("لینکدین"))
    twitter = models.URLField(blank=True, null=True, verbose_name=_("توییتر"))
    image = models.ImageField(upload_to="employees/", blank=True, null=True, verbose_name=_("تصویر"))  # اضافه شده

    def __str__(self):
        return self.name
    

class Image(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="images", verbose_name=_("شرکت"))
    image = models.ImageField(upload_to='company_images/', verbose_name=_("تصویر"))
    description = models.TextField(verbose_name=_("توضیحات"))

    def __str__(self):
        return f"Image for {self.company.name}"


class Slider(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("عنوان تصویر"))
    image = models.ImageField(upload_to="sliders/", verbose_name=_("تصویر"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("تاریخ ایجاد"))

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("عنوان مقاله"))
    image = models.ImageField(upload_to="articles/", verbose_name=_("تصویر مقاله"))
    summary = models.TextField(verbose_name=_("خلاصه مقاله"))
    content = models.TextField(verbose_name=_("محتوای مقاله"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("تاریخ ایجاد"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("آخرین بروزرسانی"))

    def __str__(self):
        return self.title


class CompanyInfo(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("عنوان شرکت"))
    description = models.TextField(verbose_name=_("توضیحات"))
    image = models.ImageField(upload_to="company_info/", blank=True, null=True, verbose_name=_("تصویر شرکت"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("تاریخ ایجاد"))

    def __str__(self):
        return self.title

class Product(models.Model):
    title_en = models.CharField(max_length=200, verbose_name=_("عنوان انگلیسی"), default='')  # مقدار پیش‌فرض
    title_fa = models.CharField(max_length=200, verbose_name=_("عنوان فارسی"), default='')
    title_ar = models.CharField(max_length=200, verbose_name=_("عنوان عربی"), default='')
    image = models.ImageField(upload_to='products/', verbose_name=_("تصویر"))

    class Meta:
        verbose_name = _("محصول")
        verbose_name_plural = _("products")

    def __str__(self):
        return self.title()

    def title(self):
        from django.utils.translation import get_language
        if get_language() == 'fa':
            return self.title_fa
        elif get_language() == 'ar':
            return self.title_ar
        else:
            return self.title_en


class FAQ(models.Model):
    question = models.CharField(max_length=255, verbose_name="سوال")
    answer = models.TextField(verbose_name="جواب")

    def __str__(self):
        return self.question
    class Meta:
        verbose_name = _("بخش FAQ")
        verbose_name_plural = _("FAQ section")

    def __str__(self):
        return self.question


class Feature(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class ContactInfo(models.Model):
    address_en = models.CharField(max_length=255, default="Unknown Address", blank=True)
    address_fa = models.CharField(max_length=255, default="Unknown Address", blank=True)
    address_ar = models.CharField(max_length=255, default="Unknown Address", blank=True)
    phone = models.CharField(max_length=20 , default="Unknown")
    email = models.EmailField()

    def __str__(self):
        return self.address_en or self.address_fa or self.address_ar

class Steel(models.Model):
    title_en = models.CharField(max_length=255)
    title_fa = models.CharField(max_length=255, blank=True, null=True)
    title_ar = models.CharField(max_length=255, blank=True, null=True)

    description1_en = models.TextField()
    description1_fa = models.TextField(blank=True, null=True)
    description1_ar = models.TextField(blank=True, null=True)

    description2_en = models.TextField(blank=True, null=True)
    description2_fa = models.TextField(blank=True, null=True)
    description2_ar = models.TextField(blank=True, null=True)

    image = models.ImageField(upload_to='steel_infos/', blank=True, null=True)

    def __str__(self):
        return self.title_en or "Steel Info"

class TranslatedText(models.Model):
    original_text = models.TextField(verbose_name="متن فارسی")
    translated_en = models.TextField(verbose_name="ترجمه انگلیسی", blank=True, null=True)
    translated_ar = models.TextField(verbose_name="ترجمه عربی", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        from googletrans import Translator
        translator = Translator()
        if not self.translated_en:
            self.translated_en = translator.translate(self.original_text, src='fa', dest='en').text
        if not self.translated_ar:
            self.translated_ar = translator.translate(self.original_text, src='fa', dest='ar').text
        super().save(*args, **kwargs)


class NavigationLink(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True, null=True)  # برای لینک‌ها
    file = models.FileField(upload_to='uploaded_pages/', blank=True, null=True)  # برای فایل‌های آپلود شده
    order = models.PositiveIntegerField(default=0)  # ترتیب نمایش
    is_active = models.BooleanField(default=True)  # فعال بودن لینک
    language = models.CharField(max_length=10, choices=[('fa', 'فارسی'), ('en', 'English'), ('ar', 'عربی')], default='fa')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']


class FooterInfo(models.Model):
    about_text = models.TextField(_("About Text"), help_text=_("Description about the company"))
    address = models.CharField(_("Address"), max_length=255)
    phone = models.CharField(_("Phone"), max_length=50)
    email = models.EmailField(_("Email"))
    copyright_text = models.CharField(_("Copyright Text"), max_length=255)

    def __str__(self):
        return self.about_text


from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email