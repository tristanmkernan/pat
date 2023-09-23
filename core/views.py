from datetime import timedelta

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    TemplateView,
    UpdateView,
)
from django_tables2 import RequestConfig
from guardian.shortcuts import get_objects_for_user

from core.data_views import (
    get_common_accomplishment_tags_for_user,
    get_common_compliment_tags_for_user,
)
from core.services import make_activity_calendars

from .filters import AccomplishmentFilter
from .forms import (
    AccomplishmentForm,
    AccomplishmentDeleteForm,
    ComplimentForm,
    ComplimentDeleteForm,
)
from .models import Accomplishment, Compliment
from .tables import AccomplishmentTable


class IndexView(TemplateView):
    template_name = "core/index.html"


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "core/dashboard.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        base_accomplishment_qs = get_objects_for_user(
            self.request.user, "core.view_accomplishment"
        )
        base_compliment_qs = get_objects_for_user(
            self.request.user, "core.view_compliment"
        )
        week_ago = (timezone.now() - timedelta(days=7)).date()

        active_dates = set(
            base_accomplishment_qs.values_list("accomplishment_date", flat=True)
        )

        context_data["activity_calendars"] = make_activity_calendars(
            active_dates,
        )

        context_data["accomplishment_sections"] = [
            {
                "title": "Recent",
                "qs": base_accomplishment_qs.order_by("-created_at")[:3],
            },
            {
                "title": "Throwback",
                "qs": base_accomplishment_qs.filter(
                    accomplishment_date__lte=week_ago
                ).order_by("?")[:3],
            },
        ]

        context_data["compliment_sections"] = [
            {
                "title": "Recent",
                "qs": base_compliment_qs.order_by("-created_at")[:3],
            },
            {
                "title": "Throwback",
                "qs": base_compliment_qs.filter(
                    created_at__date__lte=week_ago
                ).order_by("?")[:3],
            },
        ]

        return context_data


class AccomplishmentListView(LoginRequiredMixin, ListView):
    template_name = "core/accomplishment/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        filter = AccomplishmentFilter(
            self.request.GET, queryset=self.get_queryset(), request=self.request
        )
        filter.form.helper = FormHelper()
        filter.form.helper.form_method = "GET"
        filter.form.helper.add_input(Submit("submit", "Filter"))

        table = AccomplishmentTable(filter.qs)
        RequestConfig(self.request).configure(table)

        context["filter"] = filter
        context["table"] = table

        return context

    def get_queryset(self):
        qs = get_objects_for_user(self.request.user, "core.view_accomplishment")

        return qs


class AccomplishmentCreateView(LoginRequiredMixin, CreateView):
    template_name = "core/accomplishment/create.html"
    model = Accomplishment
    form_class = AccomplishmentForm
    success_url = reverse_lazy("dashboard")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        kwargs["common_tags"] = get_common_accomplishment_tags_for_user(
            self.request.user
        )

        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["common_tags"] = get_common_accomplishment_tags_for_user(
            self.request.user
        )

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)

        # set owner
        self.object.owner = self.request.user

        # persist object
        self.object.save()

        # m2m
        ## Without this next line the tags won't be saved.
        form.save_m2m()

        return HttpResponseRedirect(self.get_success_url())


class AccomplishmentUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "core/accomplishment/update.html"
    model = Accomplishment
    form_class = AccomplishmentForm
    success_url = reverse_lazy("dashboard")
    slug_field = "uuid"
    slug_url_kwarg = "uuid"

    def get_queryset(self):
        return get_objects_for_user(self.request.user, "core.change_accomplishment")


class AccomplishmentDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "core/accomplishment/delete.html"
    model = Accomplishment
    form_class = AccomplishmentDeleteForm
    success_url = reverse_lazy("dashboard")
    slug_field = "uuid"
    slug_url_kwarg = "uuid"

    def get_queryset(self):
        return get_objects_for_user(self.request.user, "core.delete_accomplishment")


class ComplimentCreateView(LoginRequiredMixin, CreateView):
    template_name = "core/compliment/create.html"
    model = Compliment
    form_class = ComplimentForm
    success_url = reverse_lazy("dashboard")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        kwargs["common_tags"] = get_common_compliment_tags_for_user(self.request.user)

        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["common_tags"] = get_common_compliment_tags_for_user(self.request.user)

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)

        # set owner
        self.object.owner = self.request.user

        # persist object
        self.object.save()

        # m2m
        ## Without this next line the tags won't be saved.
        form.save_m2m()

        return HttpResponseRedirect(self.get_success_url())


class ComplimentUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "core/compliment/update.html"
    model = Compliment
    form_class = ComplimentForm
    success_url = reverse_lazy("dashboard")
    slug_field = "uuid"
    slug_url_kwarg = "uuid"

    def get_queryset(self):
        return get_objects_for_user(self.request.user, "core.change_compliment")


class ComplimentDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "core/compliment/delete.html"
    model = Compliment
    form_class = ComplimentDeleteForm
    success_url = reverse_lazy("dashboard")
    slug_field = "uuid"
    slug_url_kwarg = "uuid"

    def get_queryset(self):
        return get_objects_for_user(self.request.user, "core.delete_compliment")
