from django.urls import path

from .feeds import LatestPostsFeed
from . import views


# ? used in the url tag referens
app_name = 'blog'

# ? list with url partterns asociated with the blog app
urlpatterns = [
    # post views
    path('', views.post_list, name='post_list'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail,name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
]
