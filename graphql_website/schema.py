import graphene
import customuser.schema
from graphql_auth.schema import UserQuery, MeQuery


class Query(UserQuery,MeQuery, graphene.ObjectType):
    pass


class Mutation(customuser.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
