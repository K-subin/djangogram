from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from djangogram.users.forms import UserChangeForm, UserCreationForm

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (("User", {"fields": ("name",)}),) + auth_admin.UserAdmin.fieldsets
    list_display = ["username", "name", "is_superuser"]
    search_fields = ["name"]
'''
class ProfileInline(admin.StackedInline):
    model = Profile
    con_delete = False

class CustomUserAdmin(auth_admin.UserAdmin):
    inlines = (ProfileInline,)

# 기존의 User의 등록을 취소했다가 User와 ProfileInline을 붙임
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)'''