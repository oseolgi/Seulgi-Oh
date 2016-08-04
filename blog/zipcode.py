import os
os.environ.setdefault("DJANGO_SETTING_MODULE", "askdjango.settings")
import django
django.setup()

import csv

CSV_PATH = 'seoul.txt'

reader = csv.reader(open(CSV_PATH, 'rt', encoding='cp949'), delimiter='|')

from blog.models import Zipcode

colums = next(reader)

zipcode_list = []

for idx, row in enumerate(reader):
    data = dict(zip(colums, row))
    zipcode_data = Zipcode(city=data['시도'], road=data['도로명'], dong=data['법정동명'], gu=data['시군구'], new_zipcode=data['새우편번호'], old_zipcode=data['구우편번호'])
    zipcode_list.append(zipcode_data)
    # zipcode.sava()

    # print(data['우편번호'])
    # if idx > 1000:
    #     break

print('zipcode size : {}'.format(len(zipcode_list)))
Zipcode.objects.bulk_create(zipcode_list, 100)