from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='article', null=True)
    # 게시글-게시판 연결
    project = models.ForeignKey(Project, on_delete=models.SET_NULL,
                                related_name='article', null=True, blank=True)
    # 제목
    title = models.CharField(max_length=200, null=True)
    # 이미지
    image = models.ImageField(upload_to='article/', null=True)
    # 게시글 내용
    content = models.TextField(null=True)
    # 게시글 시간 정보(언제 작성되었는지)
    created_at = models.DateField(auto_now_add=True, null=True)

    # 좋아요 옵션
    like = models.IntegerField(default=0)