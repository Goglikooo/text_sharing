from django.db import models

# Create your models here.
class Text(models.Model):
    content = models.TextField()
    url = models.TextField()

    def __str__(self):
        return self.content