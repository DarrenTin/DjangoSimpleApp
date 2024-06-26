from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    caption = models.CharField(max_length=100)  # alt
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title[:50]

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])