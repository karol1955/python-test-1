from django.contrib import admin

# Register your models here.
from przyklad.models import Pomysl


@admin.register(Pomysl)
class PomyslAdmin(admin.ModelAdmin):
    list_display = ['nazwa', 'tresc']
    search_fields = ['nazwa' ]
    pass

