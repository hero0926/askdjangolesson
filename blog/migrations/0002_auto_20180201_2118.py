# Generated by Django 2.0.1 on 2018-02-01 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='lnglat',
            field=models.CharField(blank=True, help_text='위도, 경도를 입력하세요.', max_length=50),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(help_text='마크다운 문법을 지원합니다.', verbose_name='내용'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(help_text='포스트 제목 내용을 입력해보세요.', max_length=100, verbose_name='제목'),
        ),
    ]
