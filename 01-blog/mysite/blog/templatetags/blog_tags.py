from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe

import markdown

from ..models import Post


register = template.Library()

# ? simple_tag is used to render data in templates, just execute some code
# ? and return data to render
# @register.simple_tag(name='custom_count_tag')
@register.simple_tag()
def total_posts():
    return Post.published.count()

# ? custom tags that render an HTML template with the data
# ? how to use {% show_latest_posts 3 %}
@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(
        total_comments=Count('comments')
    ).order_by('-total_comments')[:count]


@register.filter(name='markdown')
def markdown_format(text):
    #? the task of mark_save is render HTML strings and past it to Django
    #? and Django understand that is secure
    return mark_safe(markdown.markdown(text))
