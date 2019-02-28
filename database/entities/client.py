# pylint: disable=no-name-in-module, line-too-long
"""User entity"""
from database.context import DB
from src.helpers.enums import ApplicationType


class Client(DB.Model):
    """ User Model """
    id = DB.Column(DB.Integer, primary_key=True)
    public_id = DB.Column(DB.String(7))
    secret = DB.Column(DB.String(125))
    type = DB.Column(DB.Enum(ApplicationType))
    name = DB.Column(DB.String(16))


def seed():
    """ return entity seeds"""
    entity = Client(
        public_id="5D476OC",
        secret="t$5xUlH0dFp$9sqNXr1XUOYabnIDtNYn4VWvcwOIBYS2Z8WDVQK3RrkhCGrGSgTRhKTScp6dTp0gLTlSFsdEUN5M0ZhmoEjmlITeL97v1CgYk8HzZ*ev1egsAAJUK",
        type=ApplicationType.WEB,
        name="localhost"
    )
    return entity
