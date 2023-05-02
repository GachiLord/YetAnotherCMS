from django.db import IntegrityError
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .models import Article, Comment
from uuid import uuid4
from django.utils import timezone
from django.http.response import HttpResponseNotAllowed


def sign_in(request):
    email = request.POST.get('email', '')
    passwd = request.POST.get('password', '')
    user = authenticate(request, username=email, password=passwd)
    if user is not None:
        login(request, user)
        return redirect('blog:index')
    else:
        return redirect('blog:signIn')


def sign_up(request):
    # create a user
    email = request.POST['email']
    passwd = request.POST['password']
    try:
        user = User.objects.create_user(email, email, passwd)
        user.save()
    except IntegrityError:
        # redirect if login exists
        return redirect('blog:signUp')
    # sign in
    user = authenticate(request, username=email, password=passwd)
    if user is not None:
        login(request, user)
        return redirect('blog:index')
    else:
        return redirect('blog:signUp')


def sign_out(request):
    logout(request)
    return redirect('blog:index')


def delete_user(request):
    user = request.user
    password = request.POST.get('password', '')
    if not user.is_authenticated or not user.check_password(password):
        return redirect('blog:profile', username=user.username)
    user.delete()
    return redirect('blog:index')


def change_pass(request):
    user = request.user
    if not user.is_authenticated:
        return HttpResponseNotAllowed('user is not authed')
    old_password = request.POST.get('oldPassword', '')
    new_password = request.POST.get('newPassword', '')

    if user.check_password(old_password):
        user.set_password(new_password)
        user.save()
        update_session_auth_hash(request, user)
    return redirect('blog:profile', username=user.username)


def create_article(request):
    # redirect if not authed
    if not request.user.is_authenticated:
        return HttpResponseNotAllowed('user is not authed')
    # create an article
    name = request.POST.get('article_name', '')
    content = request.POST.get('article_text', '')
    a = Article(name=name, content=content, author=request.user, public_id=uuid4().hex, publish_date=timezone.now())
    a.save()
    return redirect('blog:edit', article_id=a.public_id)


def edit_article(request, article_id):
    # redirect if not authed
    if not request.user.is_authenticated:
        return HttpResponseNotAllowed('user is not authed')
    a = get_object_or_404(Article, public_id=article_id)
    # redirect if user is not the author
    if a.author != request.user:
        return HttpResponseNotAllowed('user is not owner')
    # edit the article
    a.name = request.POST.get('article_name', a.name)
    a.content = request.POST.get('article_text', a.content)
    a.save()
    return redirect('blog:edit', article_id=article_id)


def delete_article(request, public_id):
    a = get_object_or_404(Article, public_id=public_id)

    if request.user == a.author:
        a.delete()
        return redirect('blog:myArticles')
    else:
        return HttpResponseNotAllowed('user is not owner')


def create_comment(request, public_id):
    if not request.user.is_authenticated:
        return HttpResponseNotAllowed('user is not authed')

    c = Comment(author=request.user,
                article=get_object_or_404(Article, public_id=public_id),
                text=request.POST.get('comment_text', ''))
    c.save()

    return redirect('blog:article', article_id=public_id)
