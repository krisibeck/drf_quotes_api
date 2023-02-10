from django.db import models

from django.contrib.auth.models import User

class Quote(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    quote_body = models.TextField(blank=True, null=True)
    author =  models.CharField(max_length=60)

    def __str__(self):
        return self.author
    

class Comment(models.Model):
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_body = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    quote = models.ForeignKey(Quote,
                              on_delete=models.CASCADE, 
                              related_name = 'comments')

