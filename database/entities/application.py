"""User entity"""
from database.context import DB
from src.Helpers.enums import ApplicationType

class Application(DB.Model):
    """ User Model """
    id = DB.Column(DB.Integer, primary_key=True)
    client_id = DB.Column(DB.String(7))
    client_secret = DB.Column(DB.String(125))
    client_type = DB.Column(DB.Enum(ApplicationType))
    client_name = DB.Column(DB.String(16))


    def __repr__(self):
        return '<User %r>' % self.first_name

def seed():
    """ return entity seeds"""
    entity = Application(
        client_id="5D476OC",
        client_secret="t$5xUlH0dFp$9sqNXr1XUOYabnIDtNYn4VWvcwOIBYS2Z8WDVQK3RrkhCGrGSgTRhKTScp6dTp0gLTlSFsdEUN5M0ZhmoEjmlITeL97v1CgYk8HzZ*ev1egsAAJUK",
        client_type=ApplicationType.WEB,
        client_name="localhost"
    )
    return entity
