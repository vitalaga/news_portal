from allauth.account.forms import SignupForm
from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models import Sum
from django.urls import reverse
from django.core.cache import cache


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    author_rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.user.username

    def update_rating(self):
        rate_post = Post.objects.filter(author_id=self.pk).aggregate(post_rating=Sum('post_rating'))['post_rating']
        rate_com = Comment.objects.filter(user_id=self.user).aggregate(comment_rating=Sum('comment_rating'))['comment_rating']
        rate_com_post = Comment.objects.filter(post__author__user=self.user).aggregate(comment_rating=Sum(
                                                                                'comment_rating'))['comment_rating']
        self.author_rating = rate_post * 3 + rate_com + rate_com_post
        self.save()


class Category(models.Model):
    name_category = models.CharField(max_length=100, unique=True)
    subscribers = models.ManyToManyField(User, related_name='categories')

    def __str__(self):
        return self.name_category


class Post(models.Model):
    article = 'AR'
    news = 'NE'

    OBJECT_TYPES = [
        (article, 'Статья'),
        (news, 'Новость')
    ]
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    object_type = models.CharField(max_length=2, choices=OBJECT_TYPES, default=article)
    date_post = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField('Category', through="PostCategory")
    header = models.CharField(max_length=255)
    text_post = models.TextField()
    post_rating = models.FloatField(default=0.0)

    def like(self):
        self.post_rating += 1
        self.save()

    def dislike(self):
        self.post_rating -= 1
        self.save()

    def preview(self):
        return f'{self.text_post[:124]}...'

    def __str__(self):
        return f'{self.header.title()}: {self.text_post}, {self.date_post}'

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        cache.delete(f'post-{self.pk}')


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    text_comment = models.TextField()
    date_comment = models.DateTimeField(auto_now_add=True)
    comment_rating = models.FloatField(default=0.0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def like(self):
        self.comment_rating += 1
        self.save()

    def dislike(self):
        self.comment_rating -= 1
        self.save()


class CommonSignupForm(SignupForm):

    def save(self, request):
        user = super(CommonSignupForm, self).save(request)
        common_group = Group.objects.get(name='common')
        common_group.user_set.add(user)
        return user
