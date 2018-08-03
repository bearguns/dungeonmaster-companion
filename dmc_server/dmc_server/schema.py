import graphene

import campaign_manager.schema

class Query(campaign_manager.schema.Query, graphene.ObjectType):
  pass

schema = graphene.Schema(query=Query)