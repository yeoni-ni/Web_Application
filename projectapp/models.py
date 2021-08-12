from django.db import models

# Create your models here.

class Project(models.Model):
    # 게시판 제목
    name = models.CharField(max_length=20, null=False)
    # 게시판 내용
    description = models.CharField(max_length=200, null=True, blank=True)
    # 대표 이미지 받기
    image = models.ImageField(upload_to='project/', null=False)
    # 개시판 생성 날짜
    created_at = models.DateTimeField(auto_now_add=True)