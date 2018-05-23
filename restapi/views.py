from rest_framework import generics
from django.db.models import Count

from citizens.models import *

from votes.serializers import *
from votes.models import Proposal, Comment, UserProposalPhaseVote


""" User Endpoints """


class CitizenView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = CitizenSerializer

class SingleCitizenView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    lookup_field = 'user__username'
    serializer_class = CitizenSerializer


""" Proposal Endpoints """


class ProposalView(generics.ListCreateAPIView):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer

class SingleProposalView(generics.RetrieveAPIView):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer


class MostDebatedProposalView(generics.ListAPIView):
    queryset = Proposal.objects.filter(phase__title__iexact='debate').annotate(
        comment_count=Count('comment')).order_by('-comment_count')
    serializer_class = ProposalSerializer


class MostVotedProposalView(generics.ListAPIView):
    queryset = Proposal.objects.filter(phase__title__iexact='vote').annotate(
        votes_count=Count('proposalphasevote')).order_by('-votes_count')
    serializer_class = ProposalSerializer


class DebateProposalView(generics.ListAPIView):
    queryset = Proposal.objects.filter(phase__title__iexact='debate')
    serializer_class = ProposalSerializer


class VoteProposalView(generics.ListAPIView):
    queryset = Proposal.objects.filter(phase__title__iexact='vote')
    serializer_class = ProposalSerializer


class ReviewProposalView(generics.ListAPIView):
    queryset = Proposal.objects.filter(phase__title__iexact='review')
    serializer_class = ProposalSerializer


""" Comment Endpoints """


class CommentView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        proposal = self.kwargs['proposal']
        return Comment.objects.filter(proposal__id=proposal)


class CommentNestedView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        proposal = self.kwargs['proposal']
        comment = self.kwargs['comment']
        return Comment.objects.filter(proposal__id=proposal, nest_comment__id=comment)


""" Vote Endpoints """


class ProposalReviewVoteView(generics.CreateAPIView):
    serializer_class = ProposalReviewVoteSerializer
    queryset = UserProposalPhaseVote.objects.all()
