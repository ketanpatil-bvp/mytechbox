from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import UserModel

# Register your models here.
class UserModelAdmin(BaseUserAdmin):
    list_display=('email','date_joined','last_login','is_admin','is_active')
    search_fields=('email',)
    readonly_fields=('date_joined','last_login')
    filter_horizontal=()
    list_filter=('last_login',)
    fieldsets=()



    add_fieldsets=(
        (None,{
            'classes':('wide'),
            'fields':('email','password1','password2'),
        }),
    )

    ordering=('email',)


admin.site.register(UserModel, UserModelAdmin)