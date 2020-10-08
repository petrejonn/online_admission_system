from django import forms

from .models import AdmissionPeriod, Application, WAEC, JAMB, Result


class AdmissionPeriodCreateForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.TextInput(attrs={"type": "date"}))
    end_date = forms.DateField(widget=forms.TextInput(attrs={"type": "date"}))

    class Meta:
        model = AdmissionPeriod
        fields = ("title", "start_date", "end_date")


class ApplicationCreateForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={"type": "date"}))

    class Meta:
        model = Application
        fields = fields = [
            "first_name",
            "last_name",
            "middle_name",
            "gender",
            "date_of_birth",
            "marrital_status",
            "address",
            "email",
            "phone",
            "nationality",
            "state_of_origin",
            "local_government",
            "attatched_passport",
            "degree",
            "program",
        ]


class WAECCreateForm(forms.ModelForm):
    class Meta:
        model = WAEC
        fields = ["candidate_number", "center_number", "year", "applicant"]
        widgets = {"applicant": forms.HiddenInput()}


class JAMBCreateForm(forms.ModelForm):
    class Meta:
        model = JAMB
        fields = ["score", "year", "applicant"]
        widgets = {"applicant": forms.HiddenInput()}


class StatusForm(forms.Form):
    email = forms.EmailField()

    class Meta:
        fields = ["email"]


class ResultCreateForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = [
            "waec",
            "subject_1",
            "grade_1",
            "subject_2",
            "grade_2",
            "subject_3",
            "grade_3",
            "subject_4",
            "grade_4",
            "subject_5",
            "grade_5",
            "subject_6",
            "grade_6",
            "subject_7",
            "grade_7",
            "subject_8",
            "grade_8",
            "subject_9",
            "grade_9",
        ]
        widgets = {"waec": forms.HiddenInput()}
