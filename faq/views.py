from django.shortcuts import render
from .models import Faq
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    faq = Faq.objects.all()
    page = Paginator(faq, 6)
    page_number = request.GET.get('page')
    page_obj = page.get_page(page_number)

    if request.method == "POST":
        query_name = request.POST.get('question', None)
        if query_name:
            results = Faq.objects.filter(question__icontains=query_name)
            return render(request, 'index_faq.html', {"results":results})
    
    return render(request, 'index_faq.html', {'faq':page_obj})
    
