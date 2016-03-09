from django.db import models
from django.contrib.auth.models import User

class BlogEntry(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    hidden = models.BooleanField(default=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.text

    def edit(self,text):
        self.text = text
