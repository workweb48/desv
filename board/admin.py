from django.contrib import admin
from .models import Board,Topic,Slide_Advertising,Up_img,Topic_Advertising
# Register your models here.


admin.site.site_header = "لوحة التحكم"
admin.site.site_title = "لوحة التحكم "
# admin.site.index_title = "مرحبا بك في لوحة التحكم"

class topicAdmin(admin.ModelAdmin):
    list_display = ("title", "created_by", "board",'created_dt')
    list_filter = ("board", 'created_dt')
    search_fields = ["title", "created_by__first_name","created_by__last_name",'created_dt','created_by__username']

admin.site.register(Topic,topicAdmin),


admin.site.register(Board),

admin.site.register(Slide_Advertising),

admin.site.register(Topic_Advertising),



admin.site.register(Up_img),