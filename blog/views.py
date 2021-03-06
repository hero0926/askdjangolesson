from django.shortcuts import render, get_object_or_404
from .models import Post

from django.http import Http404

# Create your views here.
def post_list(request):
	# 경로 앞에 앱이름을 항상 표시하는 버릇
	qs = Post.objects.all()

	q = request.GET.get("q", "")
	if q :
		qs = qs.filter(title__icontains=q)
	return render(request, "blog/post_list.html", {"post_list" : qs, "q" : q})


def post_detail(request, id) :
	#try :
	#	post = Post.objects.get(id=id)
	#
	#except Post.DoesNotExist :
	#		raise Http404

	post = get_object_or_404(Post, id=id)

	return render(request, "blog/post_detail.html", {"post" : post})

