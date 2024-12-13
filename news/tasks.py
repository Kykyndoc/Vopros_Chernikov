from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from .models import Post, Category
import datetime


@shared_task
def send_notification_email(post_id):
    post = Post.objects.get(id=post_id)
    subscribers = set(
        Category.objects.filter(name__in=post.postCategory.all()).values_list('subscribers__email', flat=True))

    html_content = render_to_string('post_created_email.html', {'post': post})

    msg = EmailMultiAlternatives(
        subject=f'Новая статья: {post.title}',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@shared_task
def my_job():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(dateCreation__gte=last_week)
    categories = set(posts.values_list('postCategory__name', flat=True))
    subscribers = set(Category.objects.filter(name__in=categories).values_list('subscribers__email', flat=True))

    html_content = render_to_string('daily_post.html', {'posts': posts})

    msg = EmailMultiAlternatives(
        subject='Статьи за неделю',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()