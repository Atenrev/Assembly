from rest_framework import serializers
from .models import Proposal


class ProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = ('id', 'title', 'image', 'description', 'close_date',
                  'phase', 'user')
        read_only_fields = ('close_date', 'phase', 'user')
