from django.contrib import admin

from contracts.models import Agreement


@admin.register(Agreement)
class AgreementAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']
