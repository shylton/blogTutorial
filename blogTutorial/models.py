from django.db import models
from django.utils import timezone
from django.urls import reverse  # returns url as string
from django.contrib.auth.models import User


# ORM = Object Relational Mapper. Django uses objects to build db independent
#    of the backend! ex, can develop with sqlite then use postgres no prob!

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogTutorial:post-detail', kwargs={'pk': self.pk})

