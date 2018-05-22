from rest_framework import generics
from votes.serializers import ProposalSerializer
from votes.models import Proposal


class ProposalView(generics.ListCreateAPIView):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer
