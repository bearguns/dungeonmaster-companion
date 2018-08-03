import graphene
from graphene_django.types import DjangoObjectType

from campaign_manager.models import Campaign, Session


class CampaignType(DjangoObjectType):
    class Meta:
        model = Campaign


class SessionType(DjangoObjectType):
    class Meta:
        model = Session


class Query(object):
    all_campaigns = graphene.List(CampaignType)
    all_sessions = graphene.List(SessionType)

    def resolve_all_campaigns(self, info, **kwargs):
        return Campaign.objects.all()

    def resolve_all_related_sessions(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return Campaign.objects.select_related('sessions').all()