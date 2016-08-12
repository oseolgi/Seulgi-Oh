from django.db import models

from django.shortcuts import get_object_or_404

class Trainer(models.Model):
    trainer_id = models.CharField(max_length=100)#회원 가입 시 아이디를 가져온다.
    trainer_name = models.CharField(max_length=100)#회원의 이름(또는 닉네임)을 가져온다.
    trainer_regdate = models.DateField()#회원의 가입 일시를 가져온다.

    def __str__(self):
        return self.trainer_name

class Pokemon(models.Model):
    pokemon_name = models.CharField(max_length=100)
    pokemon_type = models.CharField(max_length=100)#정해져 있는 유형에서 선택한다.

    def __str__(self):
        return self.pokemon_name

class Capture(models.Model):
    trainer = models.ForeignKey(Trainer)
    pokemon = models.ForeignKey(Pokemon)
    location = models.CharField(max_length=200)
    date = models.DateField()

# class Ranking(models.Model):
#     rank =
#     trainer =
#     pokemon_list =

# '{}가 {}에서 {}포켓몬 {}를 잡았다.'의 형태로 뉴스를 만들고 싶다.
# 그런데 ForeignKey를 여러 개를 사용해서인지, 아니면 중복이 가능한 항목들이라 모호해서 그런지 오류가 난다.
# 하나의 pk에 대한 여러 데이터를 가져오는 것은 어떻게 하는 거지?
# 예를 들어, id가 1인 트레이너가 잡은 포켓몬의 정보라든지 ..

# class News(models.Model):
#     trainer_name = models.ForeignKey('trainer_name.Trainer')
#     pokemon_type = models.ForeignKey('pokemon_type.Pokemon')
#     pokemon_name = models.ForeignKey('pokemon_name.Pokemon')
#     caught_at = models.ForeignKey('caught_at.Pokemon')

#     def __str__(self):
#         return self.pokemon_name

# Create your models here.
