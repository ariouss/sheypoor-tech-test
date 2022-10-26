from django.db import models


class Comment(models.Model):
    post_id = models.IntegerField(default=1)
    user_id = models.IntegerField(default=1)
    message = models.TextField()
    parent_id = models.ForeignKey('self', related_name='reply_set', null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
