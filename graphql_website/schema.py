import graphene
# import customuser.schema
# from graphql_auth.schema import UserQuery, MeQuery
import blog.schema
# user
# class Query(UserQuery,MeQuery, graphene.ObjectType):
#     pass


# class Mutation(customuser.schema.Mutation, graphene.ObjectType):
#     pass


# schema = graphene.Schema(query=Query, mutation=Mutation)
# blog
class Query(blog.schema.Query, graphene.ObjectType):
    pass


class Mutation(blog.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
