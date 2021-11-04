from django.contrib import admin

# Register your models here.
from .models import AddLokasi, Pulau, Vaksin
admin.site.register(AddLokasi)
admin.site.register(Pulau)
admin.site.register(Vaksin)