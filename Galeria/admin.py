from django.contrib import admin
from Galeria.models import Fotografia

class listando_fotografias(admin.ModelAdmin):
    list_display = ('nome', 'id', 'legenda', 'categoria', 'publicado')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_editable = ('publicado',)
    list_filter = ('categoria',)

admin.site.register(Fotografia, listando_fotografias)