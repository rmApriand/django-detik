from django.contrib import admin
from .models import Berita


class BeritaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Berita, BeritaAdmin)

