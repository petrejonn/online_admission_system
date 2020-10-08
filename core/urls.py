from django.urls import path
from django.contrib.auth import views as auth_views


from . import views

app_name = "core"

urlpatterns = [
    path(r"", views.HomeView.as_view(), name="home"),
    path(r"dashboard", views.DashboardView.as_view(), name="dashboard"),
    path(
        r"dashboard/course/create",
        views.CourseCreateView.as_view(),
        name="course_create",
    ),
    path(
        r"dashboard/course/edit/<int:pk>",
        views.CourseUpdateView.as_view(),
        name="course_edit",
    ),
    path(
        r"dashboard/course/delete/<int:pk>",
        views.CourseDeleteView.as_view(),
        name="course_delete",
    ),
    path(r"dashboard/course", views.CourseListView.as_view(), name="course_list"),
    path(
        r"dashboard/admission/create",
        views.AdmissionPeriodeCreateView.as_view(),
        name="admission_create",
    ),
    path(
        r"dashboard/admission/edit/<int:pk>",
        views.AdmissionPeriodeUpdateView.as_view(),
        name="admission_edit",
    ),
    path(
        r"dashboard/admission/delete/<int:pk>",
        views.AdmissionPeriodeDeleteView.as_view(),
        name="admission_delete",
    ),
    path(
        r"dashboard/applicant",
        views.ApplicantListView.as_view(),
        name="applicant_list",
    ),
    path(
        r"dashboard/applicant/<uuid:ref>",
        views.ApplicantDetailView.as_view(),
        name="applicant_detail",
    ),
    path(
        r"dashboard/admission",
        views.AdmissionPeriodListView.as_view(),
        name="admission_list",
    ),
    path(r"apply", views.ApplyFirstCreateView.as_view(), name="apply"),
    path(r"apply2/<uuid:ref>", views.ApplySecondCreateView.as_view(), name="apply2"),
    path(r"apply3/<uuid:ref>", views.ApplyThirdCreateView.as_view(), name="apply3"),
    path(r"apply4/<int:res>", views.ApplyFourthCreateView.as_view(), name="apply4"),
    path(r"check_status", views.CheckStatusFormView.as_view(), name="check_status"),
    path(
        r"admission_status/<str:email>",
        views.AdmissionStatusDetailView.as_view(),
        name="admission_status",
    ),
    #     path(r"form/list", views.ApplicationListView.as_view(), name="list_applicants"),
    #     path(
    #         r"form/<uuid:ref>/",
    #         views.ApplicationDetailView.as_view(),
    #         name="submitted_form",
    #     ),
    #     path(
    #         r"form/<uuid:ref>/process", views.ApplicationAdmitView.as_view(), name="process"
    #     ),
    path(r"accounts/login/", auth_views.LoginView.as_view(), name="login"),
]
