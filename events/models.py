from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

CATEGORY_CHOICES = [
    ('TECHNOLOGY', 'Technology'),
    ('MUSIC & ENTERTAINMENT', 'Music & Entertainment'),
    ('FOOD', 'Food'),
    ('DANCE', 'Dance'),
    ('OTHERS', 'Others'),
]


class Event(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, blank=True)
    category = models.CharField(max_length=25, choices=CATEGORY_CHOICES, default='MUSIC')
    details = models.TextField(max_length=500)
    venue = models.CharField(max_length=50)
    date = models.DateField(help_text='Please use the following format: <em>YYYY-MM-DD</em>.')
    time = models.TimeField(help_text='Please use the following format: <em>HH:MM:SS<em>')
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_archive = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)
