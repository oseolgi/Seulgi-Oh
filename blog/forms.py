from django import forms
from .models import Location, Comment, Post
from .widgets import DaumMapWidget
'''LocationNameWidget'''


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'
        widgets = {
            'latlng': DaumMapWidget,
            # 'location_name': LocationNameWidget,
        }


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message', 'author', 'jjal']