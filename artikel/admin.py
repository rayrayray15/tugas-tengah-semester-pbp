from django.contrib import admin

from .models import Artikel

class ArtikelAdmin(admin.ModelAdmin):
    list_display = ('title', 'body','pub_date', 'image_file', 'image_url')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Artikel, ArtikelAdmin)