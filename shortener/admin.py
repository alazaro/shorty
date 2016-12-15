from django.contrib import admin

from . import models


class ShortURLAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.ShortURL, ShortURLAdmin)
