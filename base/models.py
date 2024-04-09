from django.db import models
from django.contrib.auth.models import User

class tasklist(models.Model):
    user_auth = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField()
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)


