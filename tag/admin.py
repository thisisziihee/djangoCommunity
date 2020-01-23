from django.contrib import admin
from .models import Tag

class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'registered_date',)

admin.site.register(Tag, TagAdmin)