import random

def private_key(p):
    private = random.randint(1, p)
    return private
    
def public_key(p, g, private):
    public = g**private % p
    return public
    
def secret(p, public, private):
    return public**private % p
