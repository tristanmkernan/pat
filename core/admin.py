from django.contrib import admin
from guardian.admin import GuardedModelAdmin

from .models import Accomplishment, Compliment


class AccomplishmentAdmin(GuardedModelAdmin):
    list_display = (
        "uuid",
        "owner",
        "name",
        "created_at",
    )

    list_select_related = ("owner",)


class ComplimentAdmin(GuardedModelAdmin):
    list_display = (
        "uuid",
        "owner",
        "source",
        "created_at",
    )

    list_select_related = ("owner",)


admin.site.register(Accomplishment, AccomplishmentAdmin)
admin.site.register(Compliment, ComplimentAdmin)
