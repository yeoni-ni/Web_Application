from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    # user와 profile 1 대 1일 연결
    # (User, 속성) → 계정 삭제 시 = 모델. 종속(연결 된 profile 동시 삭제), 유저 객체 접근 이름 설정,
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # 이미지(별도 폴더 profile 생성 후 주소 설정, 이미지 유무 )
    image = models.ImageField(upload_to='profile/', null=True)
    # 닉네임 모델.문자열 필드(최대 길이, 고유값(유일값) ,null)
    nickname = models.CharField(max_length=30, unique=True, null=True)
    # 메세지
    message = models.CharField(max_length=200, null=True)