from django.contrib import admin

from .models import Accomplishment


class AccomplishmentAdmin(admin.ModelAdmin):
    list_display = (
        "uuid",
        "owner",
        "name",
        "created_at",
    )

    list_select_related = ("owner",)


admin.site.register(Accomplishment, AccomplishmentAdmin)
