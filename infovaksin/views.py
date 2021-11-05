from django.http import JsonResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .forms import NewCommentForm

# Create your views here.
def index(request):
    context = {}

    form = NewCommentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/infovaksin")
    
    context['form'] = form
    return render(request,'infovaksin.html',context)

# def show_json(request):
#     return JsonResponse()

def vaksindata(request) :
    data = [
    {
      "name": "Sinovac",
      "syarat" : ["Umur 18 - 70 Tahun", "Tidak sedang mengandung", "Tidak sedang sakit"],
      "dosis": "2 kali dengan jarak 14 hari. Dosis dalam sekali suntik 0,5 ml",
      "efek" : ["bengkak di daerah bekas suntik", "Demam", "Nyeri Otot", "Sakit kepala"]
    },
    {
        "name": "Astrazeneca",
        "syarat" : ["Umur 18 - 70 Tahun", "Tidak sedang mengandung", "Tidak sedang sakit"],
        "dosis": "2 kali dengan jarak 14 hari. Dosis dalam sekali suntik 0,5 ml",
        "efek" : ["bengkak di daerah bekas suntik", "Demam", "Nyeri Otot", "Sakit kepala"]
    },
    {
        "name": "Sinopharm",
        "syarat" : ["Umur 18 - 70 Tahun", "Tidak sedang mengandung", "Tidak sedang sakit"],
        "dosis": "2 kali dengan jarak 14 hari. Dosis dalam sekali suntik 0,5 ml",
        "efek" : ["bengkak di daerah bekas suntik", "Demam", "Nyeri Otot", "Sakit kepala"]
    },
    {
        "name": "Moderna",
        "syarat" : ["Umur 18 - 70 Tahun", "Tidak sedang mengandung", "Tidak sedang sakit"],
        "dosis": "2 kali dengan jarak 14 hari. Dosis dalam sekali suntik 0,5 ml",
        "efek" : ["bengkak di daerah bekas suntik", "Demam", "Nyeri Otot", "Sakit kepala"]
    },
    {
        "name": "Pfizer",
        "syarat" : ["Umur 18 - 70 Tahun", "Tidak sedang mengandung", "Tidak sedang sakit"],
        "dosis": "2 kali dengan jarak 14 hari. Dosis dalam sekali suntik 0,5 ml",
        "efek" : ["bengkak di daerah bekas suntik", "Demam", "Nyeri Otot", "Sakit kepala"]
    },
    {
        "name": "Novavax",
        "syarat" : ["Umur 18 - 70 Tahun", "Tidak sedang mengandung", "Tidak sedang sakit"],
        "dosis": "2 kali dengan jarak 14 hari. Dosis dalam sekali suntik 0,5 ml",
        "efek" : ["bengkak di daerah bekas suntik", "Demam", "Nyeri Otot", "Sakit kepala"]
    }
  ]
    return JsonResponse({'datas' : data})

# def post_comment(request, post):
#     comments = post.comments.filter(status=True)

#     user_comment = None

#     if request.method == 'POST':
#         comment_form = NewCommentForm(request.POST)
#         if comment_form.is_valid():
#             user_comment = comment_form.save(commit=False)
#             # user_comment.post = post
#             user_comment.save()
#             return HttpResponseRedirect('/infovaksin')
#     else:
#         comment_form = NewCommentForm()

#     return render(request, 'infovaksin.html', 
#         {
#         'user_comment' : user_comment, 
#         'comments' : comments, 
#         'comment_form' : comment_form,
#         },
#         )

# def comment_gan(request):
#     context = {}

#     form = NewCommentForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return HttpResponseRedirect("/")
    
#     context['form'] = form
#     return render(request, 'infovaksin.html', context)