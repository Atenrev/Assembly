from django.urls import path
from rest_framework.authtoken import views as rest_framework_views
from .views import *

urlpatterns = [
    # Auth
    path('get_auth_token/', rest_framework_views.obtain_auth_token, name='api_get_auth_token'),
    # Citizens
    path('citizen/create', CreateCitizenView.as_view(), name='citizen_create'),
    path('citizen/<user__username>', SingleCitizenView.as_view(), name='citizen_record'),
    # Proposals
    path('proposal/', ProposalView.as_view(), name='proposal_create_list'),
    path('proposal/create', CreateProposalView.as_view(), name='proposal_create_list'),
    path('proposal/<int:pk>', SingleProposalView.as_view(), name='proposal_record'),
    path('proposal/most-debated/', MostDebatedProposalView.as_view(), name='most_debated_proposal'),
    path('proposal/most-voted/', MostVotedProposalView.as_view(), name='most_voted_proposal'),
    path('proposal/debating/', DebateProposalView.as_view(), name='debating_proposal'),
    path('proposal/voting/', VoteProposalView.as_view(), name='voting_proposal'),
    path('proposal/reviewing/', ReviewProposalView.as_view(), name='reviewing_proposal'),
    path('proposal/voting/vote', ProposalReviewVoteView.as_view(), name='voting_vote_proposal'),
    # Comments
    path('proposal/<int:proposal>/comment/', CommentView.as_view(), name='proposal_comment'),
    path('proposal/<int:proposal>/create-comment/', CreateCommentView.as_view(), name='proposal_comment'),
    path('proposal/<int:proposal>/comment/nested/<int:comment>', CommentNestedView.as_view(), name='proposal_comment_nested'),
]
