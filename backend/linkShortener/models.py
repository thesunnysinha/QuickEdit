# linkshortener/models.py
from django.db import models

class ShortLink(models.Model):
    long_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.short_code
