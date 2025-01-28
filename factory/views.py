from django.shortcuts import render, redirect
from django.utils.translation import get_language
from .forms import TranslatedTextForm
from .models import Slider, Article, Steel, Employee, TranslatedText , ContactInfo  
from .models import NavigationLink
from factory.models import Steel , FooterInfo

def get_footer_info():
    return FooterInfo.objects.first()


def index(request):
    sliders = Slider.objects.order_by('-created_at')[:5]  # آخرین 5 اسلایدر
    articles = Article.objects.order_by('-created_at')[:6]  # آخرین 6 مقاله
    steel_infos = Steel.objects.all()
    footer_info = get_footer_info()
    language = get_language()
    return render(request, 'index.html', {
        'sliders': sliders,
        'articles': articles,
        'footer_info':footer_info,
        'steel_infos':steel_infos,
        'language': language
    })


def about(request):
    current_language = get_language()
    footer_info = get_footer_info()
    if current_language == 'en':
        employees = Employee.objects.filter(name_en__isnull=False)
    elif current_language == 'ar':
        employees = Employee.objects.filter(name_ar__isnull=False)
    else:
        employees = Employee.objects.all()

    return render(request, 'about.html', {'employees': employees , 'footer_info':footer_info})


def contact(request):
    current_language = get_language()
    contact = ContactInfo.objects.first()

    if contact:
        if current_language == 'en':
            address = contact.address_en or "No address available in English"
        elif current_language == 'ar':
            address = contact.address_ar or "No address available in Arabic"
        else: 
            address = contact.address_fa or "آدرسی موجود نیست"
        
        phone = contact.phone or "Unknown phone"
        email = contact.email or "Unknown email"
    else:
        # مقادیر پیش‌فرض در صورتی که هیچ آبجکتی وجود نداشته باشد
        address = "No address available"
        phone = "Unknown phone"
        email = "Unknown email"

    footer_info = get_footer_info()

    context = {
        'address': address,
        'phone': phone,
        'email': email,
        'footer_info': footer_info
    }

    return render(request, 'contact.html', context)

from .models import Product


def product_view(request):
    products = Product.objects.all()
    language = get_language()  # دریافت زبان فعلی
    
    footer_info = get_footer_info()
    context = {
        'footer_info':footer_info
    }
    return render(request, 'products.html', context , {'products': products, 'language': language})



def translate_text(request):
    if request.method == 'POST':
        form = TranslatedTextForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('translate_text')
    else:
        form = TranslatedTextForm()

    translations = TranslatedText.objects.all()
    return render(request, 'translate_text.html', {
        'form': form,
        'translations': translations,
    })


def article_list(request):
    current_language = get_language()
    if current_language == 'en':
        articles = Article.objects.filter(title_en__isnull=False)
    elif current_language == 'ar':
        articles = Article.objects.filter(title_ar__isnull=False)
    else:
        articles = Article.objects.all()

    return render(request, 'index.html', {'articles': articles})

def employee_list_view(request):
    current_language = get_language()
    if current_language == 'en':
        employees = Employee.objects.filter(name_en__isnull=False)
    elif current_language == 'ar':
        employees = Employee.objects.filter(name_ar__isnull=False)
    else:
        employees = Employee.objects.all()
    return render(request, 'about.html', {'employees': employees})


def header(request):
    print(request.LANGUAGE_CODE)  # برای بررسی زبان
    navigation_links = NavigationLink.objects.filter(language=request.LANGUAGE_CODE, is_active=True).order_by('order')
    return render(request, 'index.html', {'navigation_links': navigation_links})



from django.utils.translation import activate

def product_list_view(request):
    activate(request.LANGUAGE_CODE)

    products = Product.objects.all()
    footer_info = get_footer_info()


    return render(request, 'products.html', {'products': products})



from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomLoginForm, CustomRegisterForm
from .models import CustomUser

# ویوی لاگین
def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # آدرس صفحه اصلی
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})

# ویوی ثبت‌نام
def register_view(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # آدرس صفحه اصلی
    else:
        form = CustomRegisterForm()
    return render(request, 'register.html', {'form': form})
