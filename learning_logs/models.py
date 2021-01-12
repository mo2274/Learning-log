from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """ a topic the user is learning about """
    text = models.CharField(max_length=200)
    date_add = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Entry(models.Model):
    """ something specific learnt about a topic """
    topic_id = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        if len(self.text) > 50:
            return f"{self.text[:50]}...."
        else:
            return self.text
