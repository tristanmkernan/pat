from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from guardian.shortcuts import assign_perm, remove_perm

from ..models import Accomplishment, Compliment


@receiver(post_save, sender=Compliment)
@receiver(post_save, sender=Accomplishment)
def set_permissions(sender, instance, **kwargs):
    """
    thanks to https://dandavies99.github.io/posts/2021/11/django-permissions/
    """
    # Get permission codenames
    view = f"view_{instance._meta.model_name}"
    change = f"change_{instance._meta.model_name}"
    delete = f"delete_{instance._meta.model_name}"

    # Assign the creator all permissions
    assign_perm(view, instance.owner, instance)
    assign_perm(change, instance.owner, instance)
    assign_perm(delete, instance.owner, instance)


@receiver(pre_delete, sender=Compliment)
@receiver(pre_delete, sender=Accomplishment)
def remove_permissions(sender, instance, **kwargs):
    """
    thanks to https://dandavies99.github.io/posts/2021/11/django-permissions/
    """
    # Get permission codenames
    view = f"view_{instance._meta.model_name}"
    change = f"change_{instance._meta.model_name}"
    delete = f"delete_{instance._meta.model_name}"

    # Remove all permissions
    remove_perm(view, instance.owner, instance)
    remove_perm(change, instance.owner, instance)
    remove_perm(delete, instance.owner, instance)
