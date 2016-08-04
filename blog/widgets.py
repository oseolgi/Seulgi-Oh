from django import forms
from django.template.loader import render_to_string


class DaumMapWidget(forms.TextInput):
    def render(self, name, value, attrs):
        lat, lng = 37.4655171, 126.9519283

        if value:
            lat, lng = value.split(',')

        html = super().render(name, value, attrs)
        rendered = render_to_string('blog/daum_map_widget.html',
            {
            'lat': lat,
            'lng': lng,
            # 'id': self.attrs['id'],
        })
        return html + rendered

# class LocationNameWidget(forms.TextInput):
#     def render(self, name, value, attrs):
#         location_name = '대여 장소'

#         if value:
#             location_name = value

#         html = super().render(name, value, attrs)
#         rendered = render_to_string('blog/daum_map_widget.html',
#             {
#             'location_name': location_name,
#             # 'id': self.attrs['id'],
#         })
#         return html + rendered