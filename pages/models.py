from django.db import models


class Team(models.Model):
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    facebook_link = models.URLField(max_length=100)
    twitter_link = models.URLField(max_length=100)
    google_plus_link = models.URLField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
