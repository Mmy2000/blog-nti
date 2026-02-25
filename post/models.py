from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):

    CATEGORY_CHOICES = (
        ("Web Development", "Web Development"),
        ("Desktop Development", "Desktop Development"),
    )

    title = models.CharField(max_length=50)
    description = models.TextField(max_length=2000)
    created_at = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    email = models.EmailField(max_length=500,blank=True,null=True)
    count_views = models.IntegerField(default=0)
    category = models.CharField(choices=CATEGORY_CHOICES, default="Web Development")


    def __str__(self):
        return self.title