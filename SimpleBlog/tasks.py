from celery import shared_task
from django.utils import timezone
from .models import BlogPost

@shared_task
def publish_post(post_id):
    post = BlogPost.objects.get(id=post_id)
    post.is_published = True
    post.publish_at = timezone.now()
    post.save()