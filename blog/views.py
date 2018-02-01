from django.shortcuts import render

# Create your views here.
def post_list(request):
	# 경로 앞에 앱이름을 항상 표시하는 버릇
	return render(request, "blog/post_list.html")