# core/schema.py

import graphene
import graphql_jwt

import blog.schema


class Query(blog.schema.Query, graphene.ObjectType):
    # Combine the queries from different apps
    pass


class Mutation(blog.schema.Mutation, graphene.ObjectType):
    # Combine the mutations from different apps
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    verify_token = graphql_jwt.Verify.Field()

    pass


schema = graphene.Schema(query=Query, mutation=Mutation)