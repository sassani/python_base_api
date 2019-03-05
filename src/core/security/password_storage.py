""" Password Storage and verification tools"""
from passlib.hash import pbkdf2_sha256

def generate_password(p_text):
    """ generate hashed password from p_text"""
    return pbkdf2_sha256.hash(p_text)

def verify_password(p_text, h_text):
    """ compare p_text as plain text with h_text as hashed password"""
    return pbkdf2_sha256.verify(p_text, h_text)
