from django.contrib import admin
from .models import Phase, Proposal, Comment, UserCommentVote, ProposalPhaseVote, UserProposalPhaseVote
# Register your models here.
admin.site.register(Phase)
admin.site.register(Proposal)
admin.site.register(Comment)
admin.site.register(ProposalPhaseVote)
admin.site.register(UserProposalPhaseVote)
admin.site.register(UserCommentVote)
