# flask_sqlalchemy/schema.py
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import db_session, User as UserModel, Tweet as TweetModel


# class Department(SQLAlchemyObjectType):
#     class Meta:
#         model = DepartmentModel
#         interfaces = (relay.Node, )


# class DepartmentConnection(relay.Connection):
#     class Meta:
#         node = Department


# class Employee(SQLAlchemyObjectType):
#     class Meta:
#         model = EmployeeModel
#         interfaces = (relay.Node, )


# class EmployeeCon(relay.Connection):
#     class Meta:
#         node = Employee

class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (relay.Node, )


class UserConnection(relay.Connection):
    class Meta:
        node = User


class Tweet(SQLAlchemyObjectType):
    class Meta:
        model = TweetModel
        interfaces = (relay.Node, )


class TweetCon(relay.Connection):
    class Meta:
        node = Tweet


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # Allows sorting over multiple columns, by default over the primary key
    # all_employees = SQLAlchemyConnectionField(EmployeeCon)
    # Disable sorting over this field
    # all_departments = SQLAlchemyConnectionField(DepartmentConnection, sort=None)
    all_tweets = SQLAlchemyConnectionField(TweetCon, sort=None)
    all_users = SQLAlchemyConnectionField(UserConnection, sort=None)

schema = graphene.Schema(query=Query)