from django.contrib import admin

from .models import Accomplishment, Compliment


class AccomplishmentAdmin(admin.ModelAdmin):
    list_display = (
        "uuid",
        "owner",
        "name",
        "created_at",
    )

    list_select_related = ("owner",)


class ComplimentAdmin(admin.ModelAdmin):
    list_display = (
        "uuid",
        "owner",
        "source",
        "created_at",
    )

    list_select_related = ("owner",)


admin.site.register(Accomplishment, AccomplishmentAdmin)
admin.site.register(Compliment, ComplimentAdmin)
