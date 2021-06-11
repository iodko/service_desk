from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext, gettext_lazy as _

from accounts.models import User, Organization, Subdivision


class OrganizationDetailInline(admin.TabularInline):
    model = User.organizations.through


@admin.register(User)
class ExtendUserAdmin(UserAdmin):
    save_on_top = True
    list_display_links = ['id', 'email']
    list_display = ('id', 'last_name', 'first_name', 'patronymic', 'username', 'email', 'get_image')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('get_image', 'last_name', 'first_name', 'patronymic', 'photo', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    readonly_fields = ('get_image',)
    inlines = (OrganizationDetailInline,)
    empty_value_display = "--------"

    def get_image(self, obj):
        if not obj.photo:
            return "-"
        return mark_safe(f'<img src="{obj.photo.url}" width=100px >')

    get_image.short_description = "Фотография пользователя"


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'inn', 'kpp')
    search_fields = ['name', 'inn', 'kpp']


@admin.register(Subdivision)
class SubdivisionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']



