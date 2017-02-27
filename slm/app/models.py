# Create your models here.

from neomodel import StructuredNode, StringProperty, RelationshipTo, RelationshipFrom, config

config.DATABASE_URL = 'bolt://neo4j:neo4j@localhost:7687'


class Term(StructuredNode):
    name = StringProperty(unique_index=True)
    header = RelationshipTo('Header', 'DEFINED_IN')


class Header(StructuredNode):
    title = StringProperty(unique_index=True)
    terms = RelationshipFrom('Term', 'DEFINED_IN')
