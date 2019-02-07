from sqlalchemy import Column, Integer, Sequence, String, create_engine
from db.database import Database


class Project(Database.Base):
    __tablename__ = 'projects'
    id = Column(Integer, Sequence('project_id_seq'), primary_key=True)
    name = Column(String(15))
    address = Column(String(15))

    def __init__(self, name, address):
        self.name = name
        self.address = address


Database.Base.metadata.create_all(Database.engine)
