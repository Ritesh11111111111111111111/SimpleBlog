from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-publish_at']
    
    # post status
    @property
    def is_published(self):
        if self.publish_at and self.publish_at <= timezone.now():
            return True
        return False

    def __str__(self):
        return self.title
    
class BlogImage(models.Model):
    image = models.ImageField(upload_to='blog_images/')  # images will be uploaded to MEDIA_ROOT/blog_images
    post = models.ForeignKey(BlogPost, related_name='images', on_delete=models.CASCADE)