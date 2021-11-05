from django.shortcuts import render, redirect
from .models import AddLokasi, Pulau, Provinsi
from .forms import addLokasiForm

from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    lokasi = AddLokasi.objects.all()
    # jawa = Jawa.objects.all()
    # kalimantan = Kalimantan.objects.all()
    # sulawesi = Sulawesi.objects.all()
    # papua = Papua.objects.all()
    
    response = {'lokasi': lokasi}
    return render(request, 'indexLokasi.html', response)

@login_required(login_url="login")
def addLokasiDef(request):
    add_form = addLokasiForm(request.POST or None)
    if request.method == 'POST':
        if add_form.is_valid():
            add_form.save()

            return redirect('lokasi_vaksin')
    response = {
        'add_form': add_form
    }
    return render(request, 'addLokasi.html', response)




