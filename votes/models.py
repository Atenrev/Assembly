from uuid import uuid4
from datetime import date, timedelta
from django.db import models
from django.contrib.auth.models import User


class Phase(models.Model):
    def __str__(self):
        return str(self.title)

    slug = models.SlugField(primary_key=True)
    title = models.CharField(max_length=100, blank=False)


class Proposal(models.Model):
    def generate_filename(self, filename):
        ext = filename.split(".")[-1]
        finalname = f"{uuid4().hex}.{ext}"
        return f"proposal/{finalname}"

    def __str__(self):
        return str(self.title)

    title = models.CharField(max_length=100, blank=False)
    image = models.ImageField(upload_to=generate_filename, blank=True)
    description = models.TextField(max_length=5000, blank=False)
    close_date = models.DateField(blank=True, default=date.today() + timedelta(days=5))
    phase = models.ForeignKey(Phase, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    def __str__(self):
        return f"{self.proposal} - {self.message}"

    timestamp = models.DateTimeField(auto_now_add=True, blank=False)
    message = models.TextField(max_length=2000, blank=False)
    proposal = models.ForeignKey(Proposal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nest_comment = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True
    )


class UserProposalPhaseVote(models.Model):
    phase = models.ForeignKey(Phase, on_delete=models.CASCADE)
    proposal = models.ForeignKey(Proposal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("phase", "proposal", "user")


class ProposalPhaseVote(models.Model):
    phase = models.ForeignKey(Phase, on_delete=models.CASCADE)
    proposal = models.ForeignKey(Proposal, on_delete=models.CASCADE)
    user_pw = models.CharField(max_length=200)
    option = models.BooleanField(default=True)
    hash = models.CharField(max_length=200)
    identifier = models.CharField(max_length=200, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    salt = models.CharField(max_length=100)


class UserCommentVote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
