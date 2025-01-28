from .models import Steel , FooterInfo

def steel_industry_context(request):
    steel_info = Steel.objects.all()
    return {
        'steel_info': steel_info
    }
def footer_view(request):
    footer_info = FooterInfo.objects.first()
    return {
        'footer_info': footer_info
    }
