import django_filters
from taggit.models import Tag

from .data_views import get_tags_for_user
from .models import Accomplishment


def get_user_tags(request):
    if request is not None:
        return get_tags_for_user(request.user)

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
