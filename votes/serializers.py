from rest_framework import serializers
from .models import Proposal


class ProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = ('id', 'title', 'image', 'description',
                  'phase', 'close_date', 'user')
