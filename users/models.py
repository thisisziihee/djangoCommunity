from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=32, verbose_name = "사용자 이름")
    password = models.CharField(max_length=64, verbose_name = "비밀번호")
    useremail = models.CharField(max_length = 128, verbose_name = "사용자 이메일")
    registered_date = models.DateTimeField(auto_now_add = True, verbose_name = "등록시간")

    def __str__(self):
        return self.username

    class Meta:
        db_table = "community_user"
        verbose_name = "사용자"
        verbose_name_plural = "사용자"