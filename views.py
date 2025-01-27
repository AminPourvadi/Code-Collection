from django.shortcuts import render, redirect
from django.utils.translation import get_language
from .forms import TranslatedTextForm
from .models import Slider, Article, Steel, Employee, TranslatedText , ContactInfo  
from .models import NavigationLink
from factory.models import Steel

def index(request):
    sliders = Slider.objects.order_by('-created_at')[:5]  # آخرین 5 اسلایدر
    articles = Article.objects.order_by('-created_at')[:6]  # آخرین 6 مقاله
    steel_infos = Steel.objects.all()
    language = get_language()
    return render(request, 'index.html', {
        'sliders': sliders,
        'articles': articles,
        'steel_infos':steel_infos,
        'language': language
    })


def about(request):
    current_language = get_language()
    if current_language == 'en':
        employees = Employee.objects.filter(name_en__isnull=False)
    elif current_language == 'ar':
        employees = Employee.objects.filter(name_ar__isnull=False)
    else:
        employees = Employee.objects.all()

    return render(request, 'about.html', {'employees': employees})


def contact(request):
    current_language = get_language()

    # دریافت اطلاعات تماس
    contact_info = ContactInfo.objects.first()
    if current_language == 'en':
        address = contact_info.address_en
    elif current_language == 'ar':
        address = contact_info.address_ar
    else:  # پیش‌فرض فارسی
        address = contact_info.address_fa

    context = {
        'address': address,
        'phone': contact_info.phone,
        'email': contact_info.email,
    }
    return render(request, 'contact.html', context)

from django.shortcuts import render
from .models import Product, FAQ, Feature


def product_view(request):
    products = Product.objects.all()
    language = get_language()  # دریافت زبان فعلی
    return render(request, 'product_list.html', {'products': products, 'language': language})


def sign(request):
    return render(request, 'sign.html')


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

    return render(request, 'products.html', {'products': products})