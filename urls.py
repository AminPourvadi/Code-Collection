from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from .views import employee_list_view 
from .context_processors import steel_industry_context


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('products/', views.product_list_view, name='products'),
    path('contact/', views.contact, name='contact'),
    path('sign/', views.sign, name='sign'),
    path('about/', employee_list_view, name='employee_list'),
]

