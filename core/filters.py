import django_filters

from guardian.shortcuts import get_objects_for_user
from taggit.models import Tag

from .models import Accomplishment


def get_user_tags(request):
    if request is not None:
        base_qs = get_objects_for_user(request.user, "core.view_accomplishment")

        return Tag.objects.filter(accomplishment__in=base_qs).distinct()

    return Tag.objects.none()


class AccomplishmentFilter(django_filters.FilterSet):
    class Meta:
        model = Accomplishment
        fields = ["name", "challenge", "reward", "tags"]

    name = django_filters.CharFilter(lookup_expr="icontains")

    challenge = django_filters.RangeFilter()
    reward = django_filters.RangeFilter()

    tags = django_filters.ModelMultipleChoiceFilter(
        queryset=get_user_tags,
    )
