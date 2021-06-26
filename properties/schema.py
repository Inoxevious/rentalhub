import graphene
from graphene_django import DjangoObjectType

from properties import models
from blog import models as b_models

class OwnerType(DjangoObjectType):
    class Meta:
        model = b_models.Profile


class PropertyType(DjangoObjectType):
    class Meta:
        model = models.Property


class TagType(DjangoObjectType):
    class Meta:
        model = models.Tag


class Query(graphene.ObjectType):
    all_properties = graphene.List(PropertyType)
    owner_by_username = graphene.Field(OwnerType, username=graphene.String())
    property_by_slug = graphene.Field(PropertyType, slug=graphene.String())
    properties_by_owner = graphene.List(PropertyType, username=graphene.String())
    properties_by_tag = graphene.List(PropertyType, tag=graphene.String())

    def resolve_all_properties(root, info):
        return (
            models.Property.objects.prefetch_related("tags")
            .select_related("owner")
            .all()
        )

    def resolve_owner_by_username(root, info, username):
        return models.Profile.objects.select_related("user").get(
            user__username=username
        )

    def resolve_properties_by_slug(root, info, slug):
        return (
            models.Property.objects.prefetch_related("tags")
            .select_related("owner")
            .get(slug=slug)
        )

    def resolve_properties_by_owner(root, info, username):
        return (
            models.Property.objects.prefetch_related("tags")
            .select_related("owner")
            .filter(owner__user__username=username)
        )

    def resolve_properties_by_tag(root, info, tag):
        return (
            models.Property.objects.prefetch_related("tags")
            .select_related("owner")
            .filter(tags__name__iexact=tag)
        )


schema = graphene.Schema(query=Query)
