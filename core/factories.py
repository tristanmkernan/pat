from datetime import timedelta

import factory
from django.utils import timezone
from taggit.models import Tag

from .models import Accomplishment, Compliment


class AccomplishmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Accomplishment

    name = factory.Faker("catch_phrase")
    accomplishment_date = factory.Faker(
        "date_between",
        start_date=timezone.localdate() - timedelta(days=60),
        end_date=timezone.localdate(),
    )
    challenge = factory.Faker("pyint", min_value=0, max_value=10)
    reward = factory.Faker("pyint", min_value=0, max_value=10)
    notes = factory.Faker("paragraph")


class ComplimentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Compliment

    source = factory.Faker("name")
    description = factory.Faker("paragraph")


class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tag
        django_get_or_create = ("name",)

    name = factory.Sequence(lambda n: f"tag-{n}")
