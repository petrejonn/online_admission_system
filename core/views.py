from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    RedirectView,
    UpdateView,
    DeleteView,
    FormView,
)
from extra_views import CreateWithInlinesView, InlineFormSetFactory

from core.models import Application, Course, AdmissionPeriod, WAEC
from core.forms import (
    AdmissionPeriodCreateForm,
    ApplicationCreateForm,
    WAECCreateForm,
    JAMBCreateForm,
    ResultCreateForm,
    StatusForm,
)


class HomeView(TemplateView):
    template_name = "core/index.html"


class ApplyFirstCreateView(CreateView):
    form_class = ApplicationCreateForm
    template_name = "core/apply/page1.html"

    def get_success_url(self):
        return reverse("core:apply2", kwargs={"ref": self.object.ref})


class ApplySecondCreateView(CreateView):
    form_class = JAMBCreateForm
    template_name = "core/apply/page2.html"

    def get_initial(self):
        appl = get_object_or_404(Application, ref=self.kwargs.get("ref"))
        return {"applicant": appl}

    def get_success_url(self):
        return reverse("core:apply3", kwargs={"ref": self.request.POST["applicant"]})


class ApplyThirdCreateView(CreateView):
    form_class = WAECCreateForm
    template_name = "core/apply/page3.html"

    def get_initial(self):
        appl = get_object_or_404(Application, ref=self.kwargs.get("ref"))
        return {"applicant": appl}

    def get_success_url(self):
        return reverse("core:apply4", kwargs={"res": self.object.id})


class ApplyFourthCreateView(CreateView):
    form_class = ResultCreateForm
    template_name = "core/apply/page4.html"
    success_url = reverse_lazy("core:home")

    def get_initial(self):
        waec = get_object_or_404(WAEC, id=self.kwargs.get("res"))
        return {"waec": waec}


class CheckStatusFormView(FormView):
    form_class = StatusForm
    template_name = "core/status/form.html"

    def get_success_url(self):
        return reverse_lazy(
            "core:admission_status", kwargs={"email": self.request.POST["email"]}
        )


class AdmissionStatusDetailView(DetailView):
    model = Application
    slug_field = "email"
    slug_url_kwarg = "email"
    template_name = "core/status/detail.html"

    def get_queryset(self):
        return Application.objects.filter(email=self.kwargs.get("email"))


class ApplicationListView(LoginRequiredMixin, ListView):
    model = Application
    template_name = "core/list.html"
    context_object_name = "application_forms"


class ApplicationDetailView(DetailView):
    pk_url_kwarg = "ref"
    model = Application
    template_name = "core/detail.html"
    context_object_name = "form"


class StatusRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy(
            "core:submitted_form", kwargs={"ref": self.request.GET.get("ref")}
        )


class ApplicationAdmitView(LoginRequiredMixin, UpdateView):
    model = Application
    pk_url_kwarg = "ref"
    fields = ["status"]

    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy(
            "core:submitted_form", kwargs={"ref": self.kwargs.get("ref")}
        )


class DashboardView(ListView):
    model = Application
    template_name = "core/dashboard/index.html"


class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    template_name = "core/dashboard/course/create.html"
    success_url = reverse_lazy("core:course_list")
    fields = ["title", "faculty"]


class CourseUpdateView(LoginRequiredMixin, UpdateView):
    model = Course
    template_name = "core/dashboard/course/edit.html"
    success_url = reverse_lazy("core:course_list")
    fields = ["title", "faculty"]


class CourseDeleteView(LoginRequiredMixin, DeleteView):
    model = Course
    template_name = "core/dashboard/course/delete.html"
    success_url = reverse_lazy("core:course_list")


class CourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = "core/dashboard/course/list.html"


class AdmissionPeriodeCreateView(LoginRequiredMixin, CreateView):
    form_class = AdmissionPeriodCreateForm
    template_name = "core/dashboard/admissions/create.html"
    success_url = reverse_lazy("core:admission_list")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.staff = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class AdmissionPeriodListView(LoginRequiredMixin, ListView):
    model = AdmissionPeriod
    context_object_name = "admission_period_list"
    template_name = "core/dashboard/admissions/list.html"


class AdmissionPeriodeUpdateView(LoginRequiredMixin, UpdateView):
    form_class = AdmissionPeriodCreateForm
    model = AdmissionPeriod
    template_name = "core/dashboard/admissions/edit.html"
    success_url = reverse_lazy("core:admission_list")


class AdmissionPeriodeDeleteView(LoginRequiredMixin, DeleteView):
    model = AdmissionPeriod
    template_name = "core/dashboard/admissions/delete.html"
    success_url = reverse_lazy("core:admission_list")


class ApplicantListView(LoginRequiredMixin, ListView):
    model = Application
    template_name = "core/dashboard/applicants/list.html"


class ApplicantDetailView(LoginRequiredMixin, UpdateView):
    model = Application
    slug_field = "ref"
    slug_url_kwarg = "ref"
    fields = ["status"]
    template_name = "core/dashboard/applicants/detail.html"
    success_url = reverse_lazy("core:applicant_list")
