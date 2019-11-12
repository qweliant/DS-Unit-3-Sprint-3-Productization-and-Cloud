from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship,
                            backref)
from sqlalchemy.ext.declarative import declarative_base
from flask_appbuilder.models.mixins import ImageColumn


engine = create_engine('sqlite:///database.sqlite3', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
# We will need this for querying
Base.query = db_session.query_property()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


    def __repr__(self):
        return '<User {}>'.format(self.name)


class Tweet(Base):
    __tablename__ = 'twitter'
    id = Column(Integer, primary_key=True)
    text = Column(Unicode(300))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(
        User, 
        backref=backref(
            'tweets',  
            lazy=True
            ))
    

    def __repr__(self):
        return '<Tweet {}>'.format(self.text)