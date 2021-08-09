from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article


class Comment(models.Model):
    # 게시글이 어디와 연결되어있는지
    article = models.ForeignKey(Article, on_delete=models.SET_NULL,
                                related_name='comment', null=True)
    # 작성자 연결
    writer = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='comment', null=True)
    # 내용
    content = models.TextField(null=False)
    # 언제 댓글이 작성되었는지
    created_at = models.DateTimeField(auto_now_add=True)