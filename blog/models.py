import re
from django.db import models
from django.forms import ValidationError
from django.utils import timezone
from .validators import MinLengthValidator, MaxLengthValidator, lnglat_validator, ZipcodeValidator
from .fields import PhoneNumberField


class Post(models.Model):
    title = models.CharField(max_length=100, validators=[MinLengthValidator(4)], verbose_name='제목')
    content = models.TextField(validators=[MinLengthValidator(4)], help_text='Markdown 문법을 써주세요.')
    tag_set = models.ManyToManyField('Tag', blank=True)
    lnglat = models.CharField(max_length=50,
        validators=[lnglat_validator],
        help_text='경도,위도 포맷으로 입력')
    created_at = models.DateTimeField(default=timezone.now)
    test_field = models.IntegerField(default=10)


class Comment(models.Model):
    post = models.ForeignKey(Post)
    message = models.TextField()
    jjal = models.ImageField(blank=True)
    author = models.CharField(max_length=20)

    def __str__(self):
        return self.author


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=20)
    phone_number = PhoneNumberField()


class Zipcode(models.Model):
    city = models.CharField(max_length=20)
    road = models.CharField(max_length=20)
    dong = models.CharField(max_length=20)
    gu = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=7, validators=[ZipcodeValidator(True)], help_text="'-'를 빼고 입력해주세요.")


class Location(models.Model):
    location_name = models.CharField(max_length=50)
    latlng = models.CharField(max_length=50)

    # def location_name(self):
    #     return self.location_name

    def lat(self):
        return self.latlng.split(',')[0]

    def lng(self):
        return self.latlng.split(',')[1]