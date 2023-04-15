from django.urls import path
from .views import (
    PostsList, PostDetail, PostSearch, PostCreate, PostEdit, PostDelete, CategoriesList, upgrade_me,
    subscribe
)


urlpatterns = [
    path('', PostsList.as_view(), name="news"),
    path('<int:pk>', PostDetail.as_view(), name='news_detail'),
    path('search/', PostSearch.as_view(), name='post_search'),
    path('create/', PostCreate.as_view(), name='news_create'),
    path('articles/create/', PostCreate.as_view(), name='article_create'),
    path('<int:pk>/edit/', PostEdit.as_view(), name='news_edit'),
    path('articles/<int:pk>/edit/', PostEdit.as_view(), name='article_edit'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='news_delete'),
    path('articles/<int:pk>/delete', PostDelete.as_view(), name='articles_delete'),
    path('upgrade/', upgrade_me, name='upgrade'),

    path('categories/<int:pk>', CategoriesList.as_view(), name='category_list'),
    path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),

]