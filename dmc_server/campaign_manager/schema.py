import graphene
from graphene_django.types import DjangoObjectType

from campaign_manager.models import Campaign, Session, Player, Encounter, Monster


class CampaignType(DjangoObjectType):
    class Meta:
        model = Campaign


class SessionType(DjangoObjectType):
    class Meta:
        model = Session

class PlayerType(DjangoObjectType):
    class Meta:
        model = Player

class EncounterType(DjangoObjectType):
    class Meta:
        model = Encounter

class MonsterType(DjangoObjectType):
    class Meta:
        model = Monster

class Query(object):
    campaign = graphene.Field(CampaignType,
                              id=graphene.Int(),
                              name=graphene.String())

    campaigns = graphene.List(CampaignType)

    def resolve_campaigns(self, info, **kwargs):
        return Campaign.objects.all()

    def resolve_campaign(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Campaign.objects.get(id=id)

        if name is not None:
            return Campaign.objects.get(name=name)

        return None

    def resolve_all_related_sessions(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return Campaign.objects.select_related('sessions').all()

    def resolve_all_related_players(self, info, **kwargs):
        return Campaign.objects.select_related('players').all()

    def resolve_all_related_encounters(self, info, **kwargs):
        return Session.objects.select_related('encounters').all()
