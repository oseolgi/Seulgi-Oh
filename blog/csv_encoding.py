import csv

CSV_PATH = ''

reader = csv.reader(open(CSV_PATH, 'rt', encoding='cp949'), delimiter='|')

columns = next(reader)

for idx, row in enumerate(reader):
    data = dict(zip(columns, row))
    print(data['우편번호'])
    if idx > 1000:
        break


'''
한 번 보고 모르겠다고 놓아버리면 영원히 모른다.
알아들을 때까지 책이라도 파보자.
'''


'''
모드
read
write
append
  +
text
binary
'''