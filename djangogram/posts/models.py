from django.db import models
from djangogram.users import models as user_model
from django.urls import reverse
from imagekit.models import ImageSpecField

# auto_now_add=True --> 데이터가 생성되어 처음 저장될 대 시간 기록
# auto_now=True --> 데이터가 수정될 때마다 시간 업데이트
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
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
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='timeline_photo/%Y/%m/%d')
    caption = models.TextField(blank=True) # 제목
    # 좋아요 -> 다대다
    like = models.ManyToManyField(user_model.User, related_name='like_post', blank=True)
    favorite = models.ManyToManyField(user_model.User, related_name='favorite_post', blank=True)

    def __str__(self):
        return "text : " + self.text

    class Meta:
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse('post:detail', args=[self.id]) 

# 댓글관리
class Comment(TimeStampedModel):
    author = models.ForeignKey(
            user_model.User, 
            null=True, 
            on_delete=models.CASCADE, #외래키 user가 삭제될 때 상황
            related_name = 'comment_author'
        )
    posts = models.ForeignKey(
            Post, 
            null=True, 
            on_delete=models.CASCADE, #외래키 user가 삭제될 때 상황
            related_name = 'comment_post'
        )
    contents = models.TextField(blank=True)
