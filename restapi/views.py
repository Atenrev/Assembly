from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Count

from .permissions import *

from citizens.models import *

from votes.serializers import *
from votes.models import Proposal, Comment, UserProposalPhaseVote
from votes.controller import *


""" User Endpoints """


class CreateCitizenView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = CitizenSerializer
    authentication_classes = ()
    permission_classes = ()


class SingleCitizenView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)
    lookup_field = "user__username"
    serializer_class = CitizenSerializer


""" Proposal Endpoints """


class ProposalView(generics.ListAPIView):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer
    authentication_classes = ()
    permission_classes = ()


class CreateProposalView(generics.CreateAPIView):
    queryset = Proposal.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ProposalSerializer


class SingleProposalView(generics.RetrieveAPIView):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer
    authentication_classes = ()
    permission_classes = ()


class MostDebatedProposalView(generics.ListAPIView):
    queryset = (
        Proposal.objects.filter(phase__title__iexact="debate")
        .annotate(comment_count=Count("comment"))
        .order_by("-comment_count")
    )
    serializer_class = ProposalSerializer
    authentication_classes = ()
    permission_classes = ()


class MostVotedProposalView(generics.ListAPIView):
    queryset = (
        Proposal.objects.filter(phase__title__iexact="vote")
        .annotate(votes_count=Count("proposalphasevote"))
        .order_by("-votes_count")
    )
    serializer_class = ProposalSerializer
    authentication_classes = ()
    permission_classes = ()


class DebateProposalView(generics.ListAPIView):
    queryset = Proposal.objects.filter(phase__title__iexact="debate")
    serializer_class = ProposalSerializer
    authentication_classes = ()
    permission_classes = ()


class VoteProposalView(generics.ListAPIView):
    queryset = Proposal.objects.filter(phase__title__iexact="vote")
    serializer_class = ProposalSerializer
    authentication_classes = ()
    permission_classes = ()


class ReviewProposalView(generics.ListAPIView):
    queryset = Proposal.objects.filter(phase__title__iexact="review")
    serializer_class = ProposalSerializer
    authentication_classes = ()
    permission_classes = ()


""" Comment Endpoints """


class CommentView(generics.ListAPIView):
    serializer_class = CommentSerializer
    authentication_classes = ()
    permission_classes = ()

    def get_queryset(self):
        proposal = self.kwargs["proposal"]
        return Comment.objects.filter(proposal__id=proposal)


class CreateCommentView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        proposal = self.kwargs["proposal"]
        return Comment.objects.filter(proposal__id=proposal)


class CommentNestedView(generics.ListAPIView):
    serializer_class = CommentSerializer
    authentication_classes = ()
    permission_classes = ()

    def get_queryset(self):
        proposal = self.kwargs["proposal"]
        comment = self.kwargs["comment"]
        return Comment.objects.filter(proposal__id=proposal, nest_comment__id=comment)


""" Vote Endpoints """


class CreateProposalVotingVoteView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        message = {"detail": 'Method "GET" not allowed.'}
        return Response(message)

    def post(self, request, format=None):
        phase = request.data["phase"]
        if phase != "vote":
            return Response({"error": "Invalid format: Phase not vote."})
        try:
            r = make_vote(
                request.user,
                phase,
                request.data["proposal"],
                request.data["option"],
                request.data["user_pw"],
            )
        except Exception as e:
            return Response({"error": f"Invalid vote, missing fields: {e}"})
        if "hash" in r:
            return Response({"hash": r["hash"], "user": str(request.user)})
        else:
            return Response({"error": r["error"]})


class ProposalReviewVoteView(generics.CreateAPIView):
    serializer_class = ProposalReviewVoteSerializer
    permission_classes = (IsAuthenticated,)
    queryset = UserProposalPhaseVote.objects.all()
