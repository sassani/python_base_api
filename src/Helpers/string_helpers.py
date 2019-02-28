""" All tools related to text and strings """
import hashlib, uuid, random, string

def random_string(n: int)-> str:
    return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(n))
