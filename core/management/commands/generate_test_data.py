from django.core.management.base import BaseCommand

from authy.factories import UserFactory
from core.factories import AccomplishmentFactory, TagFactory


class Command(BaseCommand):
    help = "My shiny new management command."

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        count = 3

        for _ in range(count):
            user = UserFactory()

            self.stdout.write(f"Created user {user.email}")

            for _ in range(50):
                accomplishment = AccomplishmentFactory(owner=user)

                for _ in range(2):
                    tag = TagFactory()

                    accomplishment.tags.add(tag)

                accomplishment.save()
