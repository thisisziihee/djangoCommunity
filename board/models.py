from django.db import models

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=64, verbose_name="제목")
    contents = models.TextField(verbose_name="내용")
    registered_date = models.DateTimeField(auto_now_add=True, verbose_name = "등록 시간")
    writer = models.ForeignKey('users.Users', verbose_name = "작성자", on_delete = models.CASCADE)


    ### 태그 추가 부분 ###
    tag = models.ManyToManyField('tag.Tag', verbose_name = "태그")
    

    def __str__(self):
        return self.title

    
    class Meta:
        db_table = "community_board"
        verbose_name = "게시물"
        verbose_name_plural = "게시물"