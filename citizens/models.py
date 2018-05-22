import uuid
from django.db import models
from django.contrib.auth.models import User


class Profile (models.Model):
    def generate_filename(self, filename):
        ext = filename.split('.')[-1]
        finalname = f'{uuid.uuid4().hex}.{ext}'
        return f'media/proposal/{finalname}'

    def __str__(self):
        return str(self.user)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to=generate_filename, blank=True)
    national_id = models.CharField(max_length=30, unique=True, blank=False)
    country = models.CharField(max_length=50, blank=False)
    province = models.CharField(max_length=50, blank=False)
    city = models.CharField(max_length=50, blank=False)
