
import graphene
 
class Query(graphene.ObjectType):
    hello = graphene.String()
 
    def resolve_hello(self, info):
        return "Hello, world!"
 
schema = graphene.Schema(query=Query)
