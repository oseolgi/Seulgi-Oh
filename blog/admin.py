from django.contrib import admin
from .models import Post, Comment, Tag, Contact, Zipcode, Location
from .forms import LocationForm

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']

class LocationAdmin(admin.ModelAdmin):
    form = LocationForm
    list_display = ['location_name', 'latlng']

class ZipcodeAdmin(admin.ModelAdmin):
    list_display = ['zipcode', 'city', 'gu', 'dong', 'road']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'message', 'author']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag)
admin.site.register(Contact)
admin.site.register(Zipcode, ZipcodeAdmin)
admin.site.register(Location, LocationAdmin)

# Register your models here.
