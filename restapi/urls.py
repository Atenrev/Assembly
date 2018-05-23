from django.urls import path
from .views import * 

urlpatterns = [
    path('proposals/', ProposalView.as_view()),
    path('proposals/most-debated', MostDebatedProposalView.as_view()),
    path('proposals/most-voted', MostVotedProposalView.as_view()),
    path('proposals/debating', DebateProposalView.as_view()),
    path('proposals/voting', VoteProposalView.as_view()),
    path('proposals/reviewing', ReviewProposalView.as_view()),
]
