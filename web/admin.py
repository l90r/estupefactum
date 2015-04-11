from django.contrib import admin
from web.models import Word, Date, Page

class WordAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Word, WordAdmin)
admin.site.register(Date)
admin.site.register(Page)
