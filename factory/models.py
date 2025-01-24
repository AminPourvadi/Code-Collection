from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    website = models.URLField()

    def __str__(self):
        return self.name


class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="employees")
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField()
    linkedin = models.URLField()
    twitter = models.URLField()

    def __str__(self):
        return self.name


class Image(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='company_images/')
    description = models.TextField()

    def __str__(self):
        return f"Image for {self.company.name}"


# ---------------------------------------------------------------------------------------#


from django.db import models

class Slider(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان تصویر")
    image = models.ImageField(upload_to="sliders/", verbose_name="تصویر")
    description = models.TextField(blank=True, null=True, verbose_name="توضیحات")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان مقاله")
    image = models.ImageField(upload_to="articles/", verbose_name="تصویر مقاله")
    summary = models.TextField(verbose_name="خلاصه مقاله")
    content = models.TextField(verbose_name="محتوای مقاله")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="آخرین بروزرسانی")

    def __str__(self):
        return self.title

class CompanyInfo(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان شرکت")
    description = models.TextField(verbose_name="توضیحات")
    image = models.ImageField(upload_to="company_info/", blank=True, null=True, verbose_name="تصویر شرکت")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    def __str__(self):
        return self.title


# ---------------------------------------------------------------------------------------#


from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان محصول")
    description = models.TextField(verbose_name="توضیحات محصول")
    image = models.ImageField(upload_to='products/', verbose_name="تصویر محصول")
    price = models.PositiveIntegerField(verbose_name="قیمت", null=True, blank=True)
    dimensions = models.CharField(max_length=100, verbose_name="ابعاد", null=True, blank=True)

    def __str__(self):
        return self.title


class FAQ(models.Model):
    question = models.CharField(max_length=300, verbose_name="سوال")
    answer = models.TextField(verbose_name="پاسخ")

    def __str__(self):
        return self.question


class Feature(models.Model):
    title = models.CharField(max_length=200, verbose_name="ویژگی")
    description = models.TextField(verbose_name="توضیحات ویژگی")

    def __str__(self):
        return self.title


# ---------------------------------------------------------------------------------------#


from django.db import models

class ContactInfo(models.Model):
    office_address = models.CharField(max_length=255, verbose_name="آدرس دفتر مرکزی")
    phone_number = models.CharField(max_length=15, verbose_name="شماره تماس")
    email = models.EmailField(verbose_name="ایمیل")
    google_map_url = models.URLField(verbose_name="لینک نقشه گوگل", blank=True, null=True)

    def __str__(self):
        return f"اطلاعات تماس ({self.office_address})"
