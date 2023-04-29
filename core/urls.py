from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
    path(
        "dashboard/accomplishment/fragment/list/",
        views.AccomplishmentListFragmentView.as_view(),
        name="accomplishment_list_fragment",
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
    #     "dashboard/meme/<uuid:uuid>/content",
    #     views.MemeContentView.as_view(),
    #     name="meme_content",
    # ),
]
