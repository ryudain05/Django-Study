from gc import get_objects

from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import F
from post.models import Post
from post.forms import PostForm

def posts_view(request):
    if request.method == "GET":
        posts = Post.objects.all()
        context = {"posts": posts, "form": PostForm}
        return render(request, "post_list.html", context)
    elif request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            body = form.cleaned_data["body"]
            author_name = form.cleaned_data["author_name"]

            post = Post.objects.create(title=title, body=body, author_name=author_name)
            context = {"post": post}
            return render(request, "post_detail.html", context)

        return redirect("posts")

def post_view(request, post_id):
    post = get_object_or_404(Post, id=post_id) #get은 데이터가 없으면 에러 반환, 장고에서 지원해주는 404 에러 처리 사용가능
    context = {"post": post}
    return render(request, "post_detail.html", context)

def post_like_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.points = F("points") + 1 # post.points = F()로 들어가있음
    post.save()
    post.refresh_from_db() # DB에서 다시 불러오기
    return render(request, "post_detail.html", {"post": post})