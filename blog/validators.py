import re
from django.forms import ValidationError
from django.utils.deconstruct import deconstructible

from django.conf import settings
import requests
import xmltodict


@deconstructible
class MinLengthValidator(object):
    def __init__(self, min_length):
        self.min_length = min_length

    def __call__(self, value):
        if len(value) < min_length:
            raise ValidationError('{}글자 이상 입력해주세요.'.format(self.min_length))


@deconstructible
class MaxLengthValidator(object):
    def __init__(self, max_length):
        self.max_length = max_length

    def __call__(self, value):
        if len(value) > max_length:
            raise ValidationError('{}글자 이하로 입력해주세요.'.format(self.max_length))


def phone_number_validator(phone_number):
    if not re.match(r'^01[06789][1-9]\d{6,7}$', value):
        raise ValidationError('휴대폰 번호를 입력해주세요.')


def lnglat_validator(lnglat):
    if not re.match(r'^(\d+\.?\d*),(\d+\.?\d*)$',lnglat):
        raise forms.ValidationError('Invalid LngLat Type')

@deconstructible
class ZipcodeValidator(object):
    '우편번호 체계안내 : http://www.koreapost.go.kr/kpost/sub/subpage.jsp?contId=010101040100'

    def __init__(self, is_check_exist = False):
        self.is_check_exist = is_check_exist

    def __call__(self, zipcode):
        if not re.match(r'^([0-6]\d{4})|(\d{3}-?\d{3})$', zipcode):
            raise ValidationError('잘못된 우편번호 형식입니다.')

        if re.match(r'^\d{3}-\d{3}$', zipcode):
            raise ValidationError("'-'를 빼고 입력해주세요.")

        if self.is_check_exist:
            # self.check_exist(zipcode)
            self.check_exist_from_db(zipcode)

    # def check_exist(self, zipcode):
    #     '우체국 open api : http://biz.epost.go.kr/customCenter/custom/custom_10.jsp'

    #     params = {
    #         'regkey': settings.EPOST_API_KEY,
    #         'target': 'postNew',
    #         'query': zipcode,
    #     }
    #     xml = requests.get('http://biz.epost.go.kr/KpostPortal/openapi', params=params).text
    #     response = xmltodict.parse(xml)
    #     try:
    #         error = response['error']
    #     except KeyError:
    #         pass
    #     else:
    #         raise ValidationError('[{error_code}] {message}'.format(**error))

    def check_exist_from_db(self, zipcode):
        from blog.models import Zipcode
        if not Zipcode.objects.filter(zipcode=new_zipcode|old_zipcode).exists():
            raise ValidationError('존재하지 않는 우편번호입니다.')

    # 아래는 내가 잘못 쓴 것
    # zipcode_exist = "\seoul.csv".object.filter(새우편번호=zipcode)
    # if not zipcode_exist:
        # raise ValidationError('존재하지 않는 우편번호입니다.')




######################################################################
''' 아래는 클로저를 이용한 Validators인데, 되도록 사용하지 말 것

def min_length_validator(min_length):
    def wrap(value):
        if len(value) < min_length:
            raise ValidationError('{}글자 이상 입력해주세요.'.format(min_length))
    return wrap

def max_length_validator(max_length):
    def wrap(value):
        if len(value) > max_length:
            raise ValidationError('{}글자 이하로 입력해주세요.'.format(max_length))
    return wrap

def phone_number_validator(value):
    if not re.match(r'^01[06789][1-9]\d{6,7}$', value):
        raise ValidationError('휴대폰 번호를 입력해주세요.')

def lnglat_validator(lnglat):
    if not re.match(r'^(\d+\.?\d*),(\d+\.?\d*)$',lnglat):
        raise forms.ValidationError('Invalid LngLat Type')

'''