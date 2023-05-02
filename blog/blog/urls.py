"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views, controllers


app_name = 'blog'
urlpatterns = [
    path('', views.articles, name='index'),
    path('<int:page_index>', views.articles, name='index'),
    path('signIn', views.sign_in, name='signIn'),
    path('signUp', views.sign_up, name='signUp'),
    path('create', views.create, name='create'),

    path('profile/<str:username>', views.profile, name='profile'),
    path('edit/<str:article_id>', views.edit, name='edit'),
    path('article/<str:article_id>', views.article, name='article'),
    path('my/', views.my_articles, name='myArticles'),
    path('my/<int:page_index>', views.my_articles, name='myArticles'),

    path('action/signOut', controllers.sign_out, name='actionSignOut'),
    path('action/signIn', controllers.sign_in, name='actionSignIn'),
    path('action/signUp', controllers.sign_up, name='actionSignUp'),
    path('action/changePassword', controllers.change_pass, name='actionChangePassword'),
    path('action/deleteAccount', controllers.delete_user, name='actionDeleteAccount'),
    path('action/createArticle', controllers.create_article, name='actionCreateArticle'),
    path('action/createComment/<str:public_id>', controllers.create_comment, name='actionCreateComment'),
    path('action/deleteArticle/<str:public_id>', controllers.delete_article, name='actionDeleteArticle'),
    path('action/editArticle/<str:article_id>', controllers.edit_article, name='actionEditArticle'),
]
