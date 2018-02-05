from django.contrib import admin
from .models import Post, Comment, Tag
from django.utils.safestring import mark_safe
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ["id", "title", "content_size", "status", "created_at", "updated_at"]
	actions = ["make_published", "make_draft"]
	
	def content_size(self, post) :
		return  mark_safe('<strong>{}글자</strong>'.format(len(post.content)))

	def make_published(self, request, queryset) :
		updated_count = queryset.update(status="p")
		self.message_user(request, "{}건의 포스팅을 Published 상태로 변경합니다.".format(updated_count))


	make_published.short_description = "지정 포스팅을 Published 상태로 변경합니다."	


	def make_draft(self, request, queryset) :
		drafted_count = queryset.update(status="d")
		self.message_user(request, "{}건의 포스팅을 Draft 상태로 변경합니다.".format(drafted_count))


	make_draft.short_description = "지정 포스팅을 Draft 상태로 변경합니다."


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin) :
	pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin) :
	pass