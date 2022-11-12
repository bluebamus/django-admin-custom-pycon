from django.db import models
from member.models import Member

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)
    
    class Meta:
        verbose_name_plural = "categories"
        
    def __str__(self):
        return self.name
    
    
class Post(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name='작성자')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='카테고리')
    title = models.CharField('제목', max_length=255)
    subtitle = models.CharField('부제목', max_length=255)
    content = models.TextField('내용')
    is_deleted = models.BooleanField('삭제된 글', default=False)
    created_at = models.DateTimeField('작성일', auto_now_add=True)
    deleted_at = models.DateTimeField('삭제일', blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name='작성자')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='원본글')
    content = models.TextField()
    report_count = models.IntegerField('신고수')
    is_blocked = models.BooleanField('노출 제한', default=False)
    created_at = models.DateTimeField('작성일', auto_now_add=True)
    
    def __str__(self):
        return self.content