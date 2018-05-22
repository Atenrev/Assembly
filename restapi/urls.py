from django.urls import path
from .views import *

urlpatterns = [
    path('proposals/get-all', ProposalView.as_view()),
    path('proposals/get-most-debated', GetMostDebatedProposalView.as_view()),
    path('proposals/get-most-voted', GetMostVotedProposalView.as_view()),
    path('proposals/get-debated', GetDebateProposalView.as_view()),
    path('proposals/get-voted', GetVoteProposalView.as_view()),
    path('proposals/get-reviewed', GetReviewProposalView.as_view()),
]
