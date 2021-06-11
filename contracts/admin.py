from django.contrib import admin

from contracts.models import Agreement, Contract


@admin.register(Agreement)
class AgreementAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('number', 'organization', 'start_date', 'end_date')
    search_fields = ['name']
    filter_horizontal = ("agreements",)
