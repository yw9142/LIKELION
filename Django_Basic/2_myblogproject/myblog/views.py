from django.shortcuts import render, redirect, get_object_or_404  # redirect 추가
from .models import Post, Comment
from faker import Faker  # faker 추가
from django.utils import timezone  # timezone 추가
from .forms import PostForm


def home(request):
    posts = Post.objects
    return render(request, 'home.html', {'posts': posts})


def create10(request):
    ifake = Faker()
    for i in range(10):
        post = Post()
        post.title = ifake.name()
        post.body = ifake.sentence()
        post.pub_date = timezone.datetime.now()
        post.save()
    return redirect('/')


def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post': post_detail})


def new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('/' + str(post.id))
    else:
        form = PostForm()
        return render(request, 'new.html', {'form': form})


def edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('/' + str(post.id))
    else:
        form = PostForm(instance=post)
    return render(request, 'new.html', {'form': form})


def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('/')


def comments_create(request, post_id):
    # 댓글을 달 게시물에 대한 정보 가져오기
    post = Post.objects.get(pk=post_id)
    # form 태그에서 넘어온 댓글 내용 가져오기
    content = request.POST.get('content')

    # 댓글 생성 및 저장
    comment = Comment(post=post, content=content)
    comment.save()

    # 댓글 생성후, 디테일 페이지로 redirect시킴
    return redirect('/' + str(post.id))


def comments_delete(request, post_id, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    comment.delete()

    return redirect('/' + str(post_id))


def comments_update(request, post_id, comment_id):
    post = get_object_or_404(Post, pk=post_id)
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == 'POST':
        comment.content = request.POST.get('content')
        comment.save()
        return redirect('/' + str(post_id))

    else:
        return render(request, 'comments_update.html', {'post': post, 'comment': comment})


def like(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.user in post.like_users.all():
        post.like_users.remove(request.user)
    else:
        post.like_users.add(request.user)

    return redirect('/' + str(post.id))
