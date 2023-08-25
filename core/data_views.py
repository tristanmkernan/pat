from django.db.models import Count
from guardian.shortcuts import get_objects_for_user
from taggit.models import Tag


def get_tags_for_user(user):
    base_qs = get_objects_for_user(user, "core.view_accomplishment")

    return Tag.objects.filter(accomplishment__in=base_qs).distinct()


def get_common_tags_for_user(user, count=5):
    return (
        get_tags_for_user(user)
        .annotate(count=Count("accomplishment"))
        .order_by("-count")[:count]
    )
