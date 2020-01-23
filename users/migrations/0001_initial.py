# Generated by Django 2.0.13 on 2020-01-18 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='사용자 이름')),
                ('password', models.CharField(max_length=64, verbose_name='비밀번호')),
                ('useremail', models.CharField(max_length=128, verbose_name='사용자 이메일')),
                ('registered_date', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
            ],
            options={
                'verbose_name': '사용자',
                'verbose_name_plural': '사용자',
                'db_table': 'community_user',
            },
        ),
    ]