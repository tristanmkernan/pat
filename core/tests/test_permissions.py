import pytest
from guardian.models import UserObjectPermission

from authy.factories import UserFactory
from core.factories import AccomplishmentFactory


@pytest.mark.django_db
def test_deleting_accomplishment_removes_permissions():
    # Given
    user = UserFactory()
    accomplishment = AccomplishmentFactory(owner=user)

    # When
    accomplishment.delete()

    # Then
    permission = UserObjectPermission.objects.filter(
        user=user, permission__codename="view_accomplishment"
    ).first()

    assert permission is None
