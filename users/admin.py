from django.contrib import admin
from .models import Profile



class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user",'mobile', "active","image")
    search_fields = ["image", "user__first_name","user__last_name",'active','mobile']



admin.site.register(Profile,ProfileAdmin)