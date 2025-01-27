from modeltranslation.translator import register, TranslationOptions , translator, TranslationOptions
from parler.models import TranslatableModel, TranslatedFields
from .models import Article
from .models import Employee
from .models import Steel
from .models import Product
from .models import Feature


@register(Article)
class ArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'summary','content')


class EmployeeTranslationOptions(TranslationOptions):
    fields = ('name', 'role', 'bio')  # فیلدهایی که می‌خواهید چندزبانه شوند

translator.register(Employee, EmployeeTranslationOptions)

class SteelIndustryTranslationOptions(TranslationOptions):
    list_display = ('title','description1','description2')

translator.register(Steel, SteelIndustryTranslationOptions)

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title_en','title_fa','title_ar')  # فیلدی که باید ترجمه شود


class FeatureTranslationOptions(TranslationOptions):
    fields = ('title','description')

translator.register(Feature, FeatureTranslationOptions)