from django.contrib.sitemaps import Sitemap
from .models import Post


# https://docs.djangoproject.com/en/4.0/ref/contrib/sitemaps/

class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    
    def items(self):
        """
        method returns the QuerySet of objects to include in this sitemap
        By default, Django calls the get_absolute_url() method on each object to retrieve its URL
        """
        return Post.published.all()
    
    def lastmod(self, obj):
        """
        method receives each object returned by items() and returns the last time the object was modified.
        """
        return obj.updated