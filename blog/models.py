from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from django.urls import reverse
import markdown


class Post(models.Model):
    title = models.CharField(max_length=255)
    excerpt = models.CharField(max_length=255, blank=True, default="")
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
   
    tags = TaggableManager()

    def formatted_markdown(self):
        return markdown.markdown(self.content, extensions=['fenced_code', 'codehilite'])

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    