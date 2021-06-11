from django.contrib import admin

from tickets.models import Ticket, Status, Category, Type, Service, \
    AvailableStatus, AvailableType, AvailableService, AvailableCategory, \
    WorkDaysCount


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "organization", "title")
    list_display_links = ("id", "author")
    search_fields = ("id", "organization", "responsible")
    list_filter = ("organization",)
    autocomplete_fields = (
        "organization",
        "service",
        "category",
        "author",
        "responsible",
        "subdivision",
        "status",
        "type",
        "agreement",
    )
    filter_horizontal = ('files',)


class BaseSTCSAdmin(admin.ModelAdmin):
    """
        STCS - Status, Type, Category, Service
        Базовый класс админки для перечисленных моделей
    """

    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')


@admin.register(AvailableStatus)
class AvailableStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'status')
    list_display_links = ('id', 'status')
    search_fields = ('status',)
    filter_horizontal = ('types', 'available_statuses')


@admin.register(AvailableType)
class AvailableTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'agreement')
    list_display_links = ('id', 'agreement')
    search_fields = ('agreement',)
    filter_horizontal = ('types',)


@admin.register(AvailableService)
class AvailableServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'agreement', 'type')
    list_display_links = ('id', 'agreement')
    search_fields = ('agreement', 'type')
    filter_horizontal = ('services',)


@admin.register(AvailableCategory)
class AvailableCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'agreement')
    list_display_links = ('id', 'agreement')
    search_fields = ('agreement',)
    filter_horizontal = ('categories',)


@admin.register(WorkDaysCount)
class AvailableCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'agreement', 'interval')
    list_display_links = ('id', 'agreement', 'interval')
    search_fields = ('agreement',)


admin.site.register(Status, BaseSTCSAdmin)
admin.site.register(Type, BaseSTCSAdmin)
admin.site.register(Category, BaseSTCSAdmin)
admin.site.register(Service, BaseSTCSAdmin)


