from django.db import models


class NewArticle(models.Model):
    """Model definition for NewArticle."""
    title = models.CharField('title', max_length=80)

    class Meta:
        """Meta definition for NewArticle."""

        verbose_name = 'article'
        verbose_name_plural = 'articles'

    def __str__(self):
        """Unicode representation of NewArticle."""
        return self.title
