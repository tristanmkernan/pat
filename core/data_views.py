from django.db.models import Count
from guardian.shortcuts import get_objects_for_user
from taggit.models import Tag


def get_accomplishment_tags_for_user(user):
    base_qs = get_objects_for_user(user, "core.view_accomplishment")

    return Tag.objects.filter(accomplishment__in=base_qs).distinct()


def get_common_accomplishment_tags_for_user(user, count=5):
    return (
        get_accomplishment_tags_for_user(user)
        .annotate(count=Count("accomplishment"))
        .order_by("-count")[:count]
    )


def get_compliment_tags_for_user(user):
    base_qs = get_objects_for_user(user, "core.view_compliment")

    return Tag.objects.filter(compliment__in=base_qs).distinct()


def get_common_compliment_tags_for_user(user, count=5):
    return (
        get_compliment_tags_for_user(user)
        .annotate(count=Count("compliment"))
        .order_by("-count")[:count]
    )
