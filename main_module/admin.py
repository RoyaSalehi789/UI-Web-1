from django.contrib import admin
from django.contrib.admin import ModelAdmin

from main_module import models


class siteBannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'position']


admin.site.register(models.siteBanner, siteBannerAdmin)
