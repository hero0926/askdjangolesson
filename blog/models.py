import re
from django.db import models
from django.forms import ValidationError
from django.utils import timezone

def lnglat_validator(value):
	if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
		raise ValidationError('Invalid LngLat Type')

class Post(models.Model):
	author = models.CharField(max_length = 20)
	title = models.CharField(max_length = 100,
		verbose_name="제목", help_text="포스트 제목 내용을 입력해보세요.")
	content = models.TextField(verbose_name="내용", help_text="마크다운 문법을 지원합니다.")
	tags = models.CharField(max_length=100, blank=True)
	lnglat = models.CharField(max_length=50, 
		validators = [lnglat_validator],
		help_text="위도, 경도를 입력하세요.", blank=True)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now = True)

