from django.urls import path

from .views import (
    calculate_project_risk,
    create_project,
    delete_project,
    index,
    update_project,
)

app_name = "projects"

urlpatterns = [
    path("", index, name="index"),
    path("create/", create_project, name="create"),
    path("update/<int:id>/", update_project, name="update"),
    path("delete/<int:id>/", delete_project, name="delete"),
    path("calcule-risk/<int:id>/", calculate_project_risk, name="calcule-risk"),
]
