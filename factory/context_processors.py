from .models import Steel

def steel_industry_context(request):
    steel_info = Steel.objects.all()
    return {
        'steel_info': steel_info
    }
