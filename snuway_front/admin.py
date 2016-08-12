from django.contrib import admin


from .models import Date

class DateAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'user',
        'start',
        'end'
    ]

admin.site.register(Date, DateAdmin)