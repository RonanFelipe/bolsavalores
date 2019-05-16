from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from .forms import UserChangeForm, UserCreationForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import MyUser, Ativos, FakeUser
# Register your models here.


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('cpf', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    limited_fieldsets = (
        (None, {'fields': ('cpf',)}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('cpf', 'password1', 'password2')
        }),
    )
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = auth_admin.AdminPasswordChangeForm
    list_display = ('cpf', 'first_name', 'last_name', 'is_admin')
    list_filter = ('is_active', 'is_admin')
    search_fields = ('first_name', 'last_name', 'cpf')
    ordering = ('cpf',)
    readonly_fields = ('last_login',)
    filter_horizontal = ('groups', 'user_permissions')


admin.site.register(MyUser, UserAdmin)
admin.site.register(Ativos)
admin.site.register(FakeUser)
