import os
import time
from hashlib import blake2b


def make_vote(data):
    # TODO: Save the vote to database 
    salt = os.urandom(blake2b.SALT_SIZE)
    msg = data["phase"] + data["proposal"] + data["option"] + data["user_pw"] + str(int(time.time()))
    hash = blake2b(salt=salt)
    hash.update(msg.encode('utf-8'))
    return hash.hexdigest()
