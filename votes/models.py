import datetime, uuid

from django.db import models
from citizens.models import Profile

class Phase (models.Model):
    slug = models.SlugField(primary_key=True)
    title = models.CharField(max_length=100, blank=False)
    def __str__ (self):
        return str(self.title)

class Proposal (models.Model):
    def generate_filename(self, filename):
        ext = filename.split('.')[-1]
        finalname = '{}.{}'.format(str(uuid.uuid4().hex),ext)
        url = 'media/proposal/%s' % (finalname)
        return url
    title = models.CharField(max_length=100, blank=False)
    image = models.ImageField(upload_to=generate_filename, blank=True)
    description = models.TextField(max_length=5000, blank=False)
    close_date = models.DateField(blank=True)
    phase = models.ForeignKey(Phase, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    def __str__ (self):
        return str(self.title)

class Comment (models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, blank=False)
    message = models.TextField(max_length=2000, blank=False)
    proposal = models.ForeignKey(Proposal, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    nest_comment = models.ForeignKey('self', on_delete=models.CASCADE, blank=True)
    def __str__ (self):
        return str(self.proposal + ": " + self.id)

class UserProposalPhaseVote (models.Model):
    def get_timestamp():
        return int(datetime.datetime.now().timestamp())
    phase = models.ForeignKey(Phase, on_delete=models.CASCADE)
    proposal = models.ForeignKey(Proposal, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    option = models.BooleanField(default=True)
    unique_id = models.CharField(max_length=200)
    timestamp = models.IntegerField(default=get_timestamp)
    salt = models.CharField(max_length=100)

class UserCommentVote (models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
