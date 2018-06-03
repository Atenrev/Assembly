from math import floor
from .models import Proposal, Phase, UserProposalPhaseVote, ProposalPhaseVote
from citizens.models import Profile
from datetime import date, timedelta

phases = list(Phase.objects.all())
phases = dict(zip([p.title for p in phases], phases))


def check_proposals():
    min_review = floor(len(Profile.objects.all()) / 2)
    proposals = Proposal.objects.filter(close_date=date.today()).exclude(
        phase__title__endswith="ed"
    )

    for proposal in proposals:
        if proposal.phase == phases.get("debate"):
            next_phase(proposal)
        else:
            votes = UserProposalPhaseVote.objects.filter(
                proposal=proposal, phase=proposal.phase
            )
            print(votes)

            if proposal.phase == phases.get("review"):
                if len(votes) >= min_review:
                    next_phase(proposal)
                else:
                    discard(proposal)

            if proposal.phase == phases.get("vote"):
                upvotes = ProposalPhaseVote.filter(
                    proposal=proposal, phase=proposal.phase, option=True
                )
                if len(upvotes) > floor(len(votes) / 2):
                    aprove(proposal)
                else:
                    discard(proposal)


def next_phase(proposal):
    proposal.close_date += timedelta(days=5)
    keys = list(phases.keys())
    proposal.phase = phases.get(keys[keys.index(proposal.phase.title) + 1])
    proposal.save()


def aprove(proposal):
    proposal.phase = phases.get("approved")
    proposal.save()


def discard(proposal):
    proposal.phase = phases.get("discarded")
    proposal.save()
