from django.db import models

# Create your models here.
class Video(models.Model):
    link = models.CharField(max_length=264)

    def __str__(self):
        return self.link