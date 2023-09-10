from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
    path(
        "dashboard/accomplishment/",
        views.AccomplishmentListView.as_view(),
        name="accomplishment_list",
    ),
    path(
        "dashboard/accomplishment/create",
        views.AccomplishmentCreateView.as_view(),
        name="accomplishment_create",
    ),
    path(
        "dashboard/accomplishment/<uuid:uuid>/update",
        views.AccomplishmentUpdateView.as_view(),
        name="accomplishment_update",
    ),
    path(
        "dashboard/accomplishment/<uuid:uuid>/delete",
        views.AccomplishmentDeleteView.as_view(),
        name="accomplishment_delete",
    ),
    # path(
    #     "dashboard/compliment/",
    #     views.ComplimentListView.as_view(),
    #     name="compliment_list",
    # ),
    path(
        "dashboard/compliment/create",
        views.ComplimentCreateView.as_view(),
        name="compliment_create",
    ),
    path(
        "dashboard/compliment/<uuid:uuid>/update",
        views.ComplimentUpdateView.as_view(),
        name="compliment_update",
    ),
    path(
        "dashboard/compliment/<uuid:uuid>/delete",
        views.ComplimentDeleteView.as_view(),
        name="compliment_delete",
    ),
]
