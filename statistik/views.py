from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index_stats.html', {})
    
def index_mview(request):
    return render(request, 'index_stats_mview.html', {})