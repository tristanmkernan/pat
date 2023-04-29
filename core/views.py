from datetime import datetime

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    FormView,
)
from guardian.shortcuts import get_objects_for_user

from .forms import (
    AccomplishmentCreateForm,
    AccomplishmentUpdateForm,
    AccomplishmentDeleteForm,
)
from .models import Accomplishment


class IndexView(TemplateView):
    template_name = "core/index.html"


class DashboardView(LoginRequiredMixin, ListView):
    template_name = "core/dashboard.html"

    def get_queryset(self):
        qs = get_objects_for_user(
            self.request.user, "core.view_accomplishment"
        ).order_by("-created_at")

        return qs[:10]


class AccomplishmentListFragmentView(LoginRequiredMixin, ListView):
    template_name = "core/accomplishment/list_fragment.html"

    def get_queryset(self):
        qs = get_objects_for_user(
            self.request.user, "core.view_accomplishment"
        ).order_by("-created_at")

        after = datetime.fromisoformat(self.request.GET.get("after"))

        ## since we sort by timestamp descending, we want results which were created
        ## before the cursor
        qs = qs.filter(created_at__lt=after)

        return qs[:10]


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
