from django.db import models
from djangogram.users import models as user_model

# Create your models here.
class TimeStampedModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    # meta옵션을 주면 timestamp는 단독으로 테이블이 만들어지지 않는다.
    class Meta:
        abstract = True

class Post(TimeStampedModel):
    # 작성자=User -> 외래키 사용
    author = models.ForeignKey(
        user_model.User, 
        null=True, 
        on_delete=models.CASCADE, #외래키 user가 삭제될 때 상황
        related_name = 'post_author')
    image = models.ImageField(blank=True)
    caption = models.TextField(blank=True) # 제목
    # 좋아요 -> 다대다
    image_likes = models.ManyToManyField(user_model.User, related_name='post_image_likes')

# 댓글관리
class Comment(TimeStampedModel):
    author = models.ForeignKey(
            user_model.User, 
            null=True, 
            on_delete=models.CASCADE, #외래키 user가 삭제될 때 상황
            related_name = 'post_author'
        )
    posts = models.ForeignKey(
            Post, 
            null=True, 
            on_delete=models.CASCADE, #외래키 user가 삭제될 때 상황
            related_name = 'comment_post'
        )
    contents = models.TextField(blank=True)
