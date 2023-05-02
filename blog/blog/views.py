from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from django.contrib.auth.models import User
from django.core.paginator import Paginator


def create(request):
    if not request.user.is_authenticated:
        return redirect('blog:signIn')

    return render(request, 'blog/editor.html', {'user': request.user, 'action': 'create'})


def edit(request, article_id):
    # redirect if not authed
    if not request.user.is_authenticated:
        return redirect('/signIn')
    # get an article
    a = get_object_or_404(Article, public_id=article_id)
    # redirect if user is not the author
    if a.author != request.user:
        return redirect('blog:index')

    return render(request, 'blog/editor.html', {'user': request.user, 'action': 'edit', 'article': a})


def article(request, article_id):
    a = get_object_or_404(Article, public_id=article_id)
    cs = Comment.objects.filter(article=a).order_by('-id')
    return render(request, 'blog/article.html', {'user': request.user, 'article': a, 'comments': cs})


def articles(request, page_index=1):
    p = Paginator(Article.objects.order_by('-id'), 10)
    page = p.get_page(page_index)
    return render(request, 'blog/browse.html', {'user': request.user, 'page': page})


def my_articles(request, page_index=1):
    if not request.user.is_authenticated:
        return redirect('/signIn')

    a = Article.objects.filter(author=request.user).order_by('-id')
    p = Paginator(a, 10)
    page = p.get_page(page_index)
    return render(request, 'blog/browse.html', {'user': request.user, 'page': page, 'my': True})


def sign_in(request):
    return render(request, 'blog/signIn.html', {'user': request.user})


def sign_up(request):
    return render(request, 'blog/signUp.html', {'user': request.user})


def profile(request, username):
    user = get_object_or_404(User, username=username)
    stat = {
        'article_count': Article.objects.filter(author=user).count(),
        'comment_count': Comment.objects.filter(author=user).count(),
    }

    return render(request, 'blog/profile.html', {'user': request.user, 'stat': stat, 'profile_owner': user})
