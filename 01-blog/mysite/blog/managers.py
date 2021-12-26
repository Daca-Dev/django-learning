from django.db import models


class PublishedManager(models.Manager):
    #? replace the all() method in the Manager
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')
