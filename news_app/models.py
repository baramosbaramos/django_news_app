from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    url = models.URLField()
    good = models.IntegerField(null=True, blank=True, default=1)


    def __str__(self):
        return self.title
