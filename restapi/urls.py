from django.urls import path
from rest_framework.authtoken import views as rest_framework_views
from .views import *

urlpatterns = [
    # Citizens
    path(
        "citizen/login",
        rest_framework_views.obtain_auth_token,
        name="api_get_auth_token",
    ),
    path("citizen/create", CreateCitizenView.as_view(), name="citizen_create"),
    path("citizen/<user__username>", SingleCitizenView.as_view(), name="citizen_record"),
    # Proposals
    path("proposals", ProposalView.as_view(), name="proposals"),
    path("proposals/create", CreateProposalView.as_view(), name="proposal_create"),
    path("proposals/<int:pk>", SingleProposalView.as_view(), name="proposal_record"),
    path("proposals/voted-user-proposal/<phase>", VotedUserProposalView.as_view(), name="voted_user_proposal"),
    path(
        "proposals/most-debated",
        MostDebatedProposalView.as_view(),
        name="most_debated_proposal",
    ),
    path(
        "proposals/most-voted",
        MostVotedProposalView.as_view(),
        name="most_voted_proposal",
    ),
    path("proposals/debating", DebateProposalView.as_view(), name="debating_proposal"),
    path("proposals/voting", VoteProposalView.as_view(), name="voting_proposal"),
    path("proposals/reviewing", ReviewProposalView.as_view(), name="reviewing_proposal"),
    # Votes CreateProposalVotingVoteView
    path(
        "proposals/reviewing/vote",
        ProposalReviewVoteView.as_view(),
        name="reviewing_vote_proposal",
    ),
    path(
        "proposals/reviewing/destroy-vote/<int:pk>",
        DestroyReviewVoteView.as_view(),
        name="destroy_reviewing_vote_proposal",
    ),
    path(
        "proposals/voting/vote",
        CreateProposalVotingVoteView.as_view(),
        name="voting_vote_proposal",
    ),
    # Comments
    path(
        "proposals/<int:proposal>/comments",
        CommentView.as_view(),
        name="proposal_comment",
    ),
    path(
        "proposals/<int:proposal>/most-voted-comments",
        MostVotedCommentView.as_view(),
        name="proposal_comment",
    ),
    path(
        "proposals/<int:proposal>/create-comment",
        CreateCommentView.as_view(),
        name="create_proposal_comment",
    ),
    path(
        "proposals/<int:proposal>/vote-comment",
        UserCommentVote.as_view(),
        name="vote_proposal_comment",
    ),
    path(
        "proposals/<int:proposal>/nested-comment/<int:comment>",
        CommentNestedView.as_view(),
        name="proposal_comment_nested",
    ),
]
