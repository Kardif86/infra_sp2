from django.contrib import admin

from .models import User


class BaseAdminSettings(admin.ModelAdmin):
    empty_value_display = '-пусто-'
    list_filter = ('role', 'username')


class UsersAdmin(BaseAdminSettings):
    list_display = (
        'id',
        'username',
        'email',
        'role',
        'bio',
    )
    list_display_links = ('id', 'username')
    search_fields = ('role', 'username')


admin.site.register(User, UsersAdmin)
