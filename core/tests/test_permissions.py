import pytest
from guardian.models import UserObjectPermission

from authy.factories import UserFactory
from core.factories import AccomplishmentFactory, ComplimentFactory


@pytest.mark.django_db
@pytest.mark.parametrize(
    "factory",
    [
        AccomplishmentFactory,
        ComplimentFactory,
    ],
)
def test_creating_object_adds_permissions(factory):
    # Given
    user = UserFactory()

    # When
    instance = factory(owner=user)

    # Then
    permission_names = [
        f"view_{instance._meta.model_name}",
        f"change_{instance._meta.model_name}",
        f"delete_{instance._meta.model_name}",
    ]

    for name in permission_names:
        permission = UserObjectPermission.objects.filter(
            user=user, permission__codename=name
        ).first()

        assert permission is not None


@pytest.mark.django_db
@pytest.mark.parametrize(
    "factory",
    [
        AccomplishmentFactory,
        ComplimentFactory,
    ],
)
def test_deleting_object_removes_permissions(factory):
    # Given
    user = UserFactory()
    instance = factory(owner=user)

    # When
    instance.delete()

    # Then
    permission_names = [
        f"view_{instance._meta.model_name}",
        f"change_{instance._meta.model_name}",
        f"delete_{instance._meta.model_name}",
    ]

    for name in permission_names:
        permission = UserObjectPermission.objects.filter(
            user=user, permission__codename=name
        ).first()

        assert permission is None
