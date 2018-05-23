import hashlib
from platform import platform

def hasher(login, passw):

    hash = hashlib.shake_128()

    hash.update(login.encode())
    hash.update(passw.encode())
    hash.update(platform().encode())

    hash = hash.hexdigest(10)
    print(hash)

    return hash
