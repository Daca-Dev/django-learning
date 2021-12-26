from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

from taggit.managers import TaggableManager 

from blog.managers import PublishedManager


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    # ? unique_for_date: specify that de slug and the publish field should be unique together
    # ? we can't have to dates with the same slug
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft'
    )

    tags = TaggableManager()
    
    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.
    # ? you can replace objects directly

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Create the absolute url path of the model

        Returns:
            string: absolute url path to the model
        """
        return reverse(
            'blog:post_detail',
            args=[
                self.publish.year,
                self.publish.month,
                self.publish.day,
                self.slug
            ]
        )


class Comment(models.Model):
    # ? related_name: is re name for the variable in reverse situation, example
    # ? Post.comments.all() to get all the comments asociated to a specific user
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
