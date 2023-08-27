import django_tables2 as tables
from django.urls import reverse

from .models import Accomplishment


class AccomplishmentTable(tables.Table):
    class Meta:
        model = Accomplishment
        order_by = "-created_at"
        fields = ["name", "challenge", "reward", "notes", "tags", "accomplishment_date"]

    name = tables.Column(
        linkify=lambda record: reverse("accomplishment_update", args=[record.uuid])
    )
    tags = tables.TemplateColumn(
        """
        {% for tag in record.tags.all %}
            <span class="badge bg-secondary">{{ tag.name }}</span>
        {% endfor %}
        """,
        orderable=False,
    )
    notes = tables.Column(orderable=False)
    accomplishment_date = tables.DateColumn(verbose_name="Date")
