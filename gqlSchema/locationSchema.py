#import graphene
from graphene_mongo import  MongoengineObjectType
from resolvers.locationModel import Location as LocationModel
from graphene.relay import Node

class Location(MongoengineObjectType):

    class Meta:
        model = LocationModel
        interfaces = (Node,)

