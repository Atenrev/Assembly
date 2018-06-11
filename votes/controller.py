import os
import time
import uuid
from hashlib import blake2b

from django.db import IntegrityError
from django.contrib.auth.hashers import make_password
from .models import ProposalPhaseVote, UserProposalPhaseVote, Phase, Proposal


def make_vote(user, phase, proposal, option, user_pw):
    timestamp = str(int(time.time()))
    password_in_database = user.password.split('$')
    password = make_password(user_pw,
        hasher=password_in_database[0],
        salt=password_in_database[-2])

    if not isinstance(option, bool):
        return {"error": "Invalid format: Option not bool."}

    try:
        phase = Phase.objects.get(slug=phase)
        proposal = Proposal.objects.get(pk=proposal)
    except Exception as e:
        return {"error": f"Invalid format: {e}"}

    if proposal.phase != phase:
        return {"error": "Input phase does not correspond with the proposal's phase."}

    try:
        salt = os.urandom(blake2b.SALT_SIZE)
        msg = str(phase) + str(proposal) + str(option) + password + timestamp
        hash = blake2b(salt=salt)
        hash.update(msg.encode("utf-8"))
        digest = hash.hexdigest()

        uservote = UserProposalPhaseVote(phase=phase, proposal=proposal, user=user)
        anonvote = ProposalPhaseVote(
            phase=phase,
            proposal=proposal,
            user_pw=password,
            option=option,
            hash=digest,
            identifier=uuid.uuid4().hex,
            timestamp=timestamp,
            salt=salt,
        )

        uservote.save()
        anonvote.save()

        return {"hash": digest}
    except IntegrityError:
        return {"error": "You have already voted this proposal."}
    except Exception as e:
        return {"error": f"Error during the processing of your vote: {e}"}
