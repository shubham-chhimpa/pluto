from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from AuthEngine.forms import PlutoUserCreationForm, PlutoUserChangeForm
from AuthEngine.models import PlutoUser


class CustomUserAdmin(UserAdmin):
    add_form = PlutoUserCreationForm
    form = PlutoUserChangeForm
    model = PlutoUser
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(PlutoUser, CustomUserAdmin)
