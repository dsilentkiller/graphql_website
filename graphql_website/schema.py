import graphene
import customuser.schema
from graphql_auth import mutations
import blog.schema
# user
# class Query(UserQuery,MeQuery, graphene.ObjectType):
#     pass


# class Mutation(customuser.schema.Mutation, graphene.ObjectType):
#     pass


# schema = graphene.Schema(query=Query, mutation=Mutation)
# blog

# create user
class AuthMutation(graphene.ObjectType):
    # createuser
    register = mutations.Register.Field()


class Query(customuser.schema.Query, blog.schema.Query, graphene.ObjectType):
    pass


class Mutation(AuthMutation, customuser.schema.Mutation, blog.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
