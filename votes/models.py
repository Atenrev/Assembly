import uuid
from django.db import models
from citizens.models import Profile


class Phase (models.Model):
    def __str__(self):
        return str(self.title)

    slug = models.SlugField(primary_key=True)
    title = models.CharField(max_length=100, blank=False)


class Proposal(models.Model):
    def generate_filename(self, filename):
        ext = filename.split('.')[-1]
        finalname = f'{uuid.uuid4().hex}.{ext}'
        return f'media/proposal/{finalname}'

    def __str__(self):
        return str(self.title)

    title = models.CharField(max_length=100, blank=False)
    image = models.ImageField(max_length=2048, upload_to=generate_filename,
                              blank=True)
    description = models.TextField(max_length=5000, blank=False)
    close_date = models.DateField(blank=True)
    phase = models.ForeignKey(Phase, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)


class Comment(models.Model):
    def __str__(self):
        return f'{self.proposal} - {self.id}'

    timestamp = models.DateTimeField(auto_now_add=True, blank=False)
    message = models.TextField(max_length=2000, blank=False)
    proposal = models.ForeignKey(Proposal, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    nest_comment = models.ForeignKey('self', on_delete=models.CASCADE,
                                     blank=True)


class UserProposalPhaseVote(models.Model):
    phase = models.ForeignKey(Phase, on_delete=models.CASCADE)
    proposal = models.ForeignKey(Proposal, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    option = models.BooleanField(default=True)
    unique_id = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    salt = models.CharField(max_length=100)


class UserCommentVote(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
