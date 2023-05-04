from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    TemplateView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django_tables2 import RequestConfig
from guardian.shortcuts import get_objects_for_user

from .filters import AccomplishmentFilter
from .forms import (
    AccomplishmentCreateForm,
    AccomplishmentUpdateForm,
    AccomplishmentDeleteForm,
)
from .models import Accomplishment
from .tables import AccomplishmentTable


class IndexView(TemplateView):
    template_name = "core/index.html"


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "core/dashboard.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        base_qs = get_objects_for_user(self.request.user, "core.view_accomplishment")

        context_data["accomplishment_sections"] = [
            {
                "title": "Recent Accomplishments",
                "qs": base_qs.order_by("-created_at")[:3],
            },
            {
                "title": "Challenging Accomplishments",
                "qs": base_qs.order_by("-challenge")[:3],
            },
            {
                "title": "Rewarding Accomplishments",
                "qs": base_qs.order_by("-reward")[:3],
            },
        ]

        return context_data


# TODO filters
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
    form_class = AccomplishmentCreateForm
    success_url = reverse_lazy("dashboard")

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
    form_class = AccomplishmentUpdateForm
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
