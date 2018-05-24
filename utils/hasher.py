import hashlib
from platform import platform

from dwh.salt import salt


def hasher(login, passw):

    hash = hashlib.shake_128()

    hash.update(login.encode())
    hash.update(passw.encode())
    hash.update(platform().encode())
    hash.update(salt.encode())

    return hash.hexdigest(10)

