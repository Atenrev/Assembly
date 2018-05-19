from django.contrib import admin
from .models import Phase, Proposal, Comment, UserCommentVote, UserProposalPhaseVote
# Register your models here.
admin.site.register(Phase)
admin.site.register(Proposal)
admin.site.register(Comment)
admin.site.register(UserProposalPhaseVote)
admin.site.register(UserCommentVote)
