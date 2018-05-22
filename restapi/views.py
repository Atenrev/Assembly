from rest_framework import generics
from django.db.models import Count

from votes.serializers import ProposalSerializer
from votes.models import Proposal


"""
    Proposal Endpoints
"""
class ProposalView(generics.ListCreateAPIView):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer

class GetMostDebatedProposalView(generics.ListAPIView):
    queryset = Proposal.objects.filter(phase__title__iexact='debate').annotate(
        comment_count=Count('comment')).order_by('-comment_count')
    serializer_class = ProposalSerializer

class GetMostVotedProposalView(generics.ListAPIView):
    queryset = Proposal.objects.filter(phase__title__iexact='vote').annotate(
        votes_count=Count('proposalphasevote')).order_by('-votes_count')
    serializer_class = ProposalSerializer

class GetDebateProposalView(generics.ListAPIView):
    queryset = Proposal.objects.filter(phase__title__iexact='debate')
    serializer_class = ProposalSerializer

class GetVoteProposalView(generics.ListAPIView):
    queryset = Proposal.objects.filter(phase__title__iexact='vote')
    serializer_class = ProposalSerializer

class GetReviewProposalView(generics.ListAPIView):
    queryset = Proposal.objects.filter(phase__title__iexact='review')
    serializer_class = ProposalSerializer
