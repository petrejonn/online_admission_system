import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class Course(models.Model):
    FACULTY = [
        ("NAS", "Natural and Applied Science"),
        ("MSS", "Management and Social Science"),
    ]
    title = models.CharField(max_length=25)
    faculty = models.CharField(max_length=25, choices=FACULTY)

    def __str__(self):
        return self.title


class Application(models.Model):
    GENDER = [("Male", "Male"), ("Female", "Female")]
    MARRITAL_STATUS = [("Single", "Single"), ("Married", "Married")]
    DEGREE = [
        ("Bachelor's", "Bachelor's"),
        ("Master's", "Master's"),
        ("PHD/PG", "PHD/PG"),
    ]
    STATUS = [
        ("Review", "Under Review"),
        ("Granted", "Admission Granted"),
        ("Denied", "Admission Denied"),
    ]

    EXAM_TYPE = [("WAEC", "WAEC"), ("NECO", "NECO")]

    # Personal Dat
    ref = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    middle_name = models.CharField(max_length=25)
    gender = models.CharField(max_length=25, choices=GENDER)
    date_of_birth = models.DateField()
    marrital_status = models.CharField(max_length=25, choices=MARRITAL_STATUS)
    address = models.CharField(max_length=50)
    email = models.EmailField(max_length=25, unique=True)
    phone = models.CharField(max_length=25)
    nationality = models.CharField(max_length=25)
    state_of_origin = models.CharField(max_length=25)
    local_government = models.CharField(max_length=25)
    # attatchments
    attatched_passport = models.ImageField()
    # attatched_result = models.FileField()
    # course details
    degree = models.CharField(max_length=25, choices=DEGREE)
    program = models.OneToOneField(Course, on_delete=models.CASCADE)
    status = models.CharField(max_length=25, choices=STATUS, default="Review")

    def get_absolute_url(self):
        return reverse("core:submitted_form", kwargs={"ref": self.ref})

    def get_full_name(self):
        return self.last_name + " " + self.first_name + " " + self.middle_name


class AdmissionPeriod(models.Model):
    title = models.CharField(max_length=25)
    staff = models.OneToOneField(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title


class WAEC(models.Model):
    applicant = models.OneToOneField(
        Application, on_delete=models.CASCADE, related_name="waec"
    )
    candidate_number = models.CharField(max_length=25)
    year = models.IntegerField()
    center_number = models.CharField(max_length=25)


class Result(models.Model):
    GRADE = [
        ("A1", "A1"),
        ("B2", "B2"),
        ("B3", "B3"),
        ("C4", "C4"),
        ("C5", "C5"),
        ("C6", "C6"),
        ("D7", "D7"),
        ("E8", "E8"),
        ("F9", "F9"),
    ]
    waec = models.OneToOneField(WAEC, on_delete=models.CASCADE)
    subject_1 = models.CharField(max_length=50,)
    grade_1 = models.CharField(max_length=2, choices=GRADE)
    subject_2 = models.CharField(max_length=50)
    grade_2 = models.CharField(max_length=2, choices=GRADE)
    subject_3 = models.CharField(max_length=50)
    grade_3 = models.CharField(max_length=2, choices=GRADE)
    subject_4 = models.CharField(max_length=50)
    grade_4 = models.CharField(max_length=2, choices=GRADE)
    subject_5 = models.CharField(max_length=50)
    grade_5 = models.CharField(max_length=2, choices=GRADE)
    subject_6 = models.CharField(max_length=50)
    grade_6 = models.CharField(max_length=2, choices=GRADE)
    subject_7 = models.CharField(max_length=50)
    grade_7 = models.CharField(max_length=2, choices=GRADE)
    subject_8 = models.CharField(max_length=50, blank=True)
    grade_8 = models.CharField(max_length=2, choices=GRADE, blank=True)
    subject_9 = models.CharField(max_length=50, blank=True)
    grade_9 = models.CharField(max_length=2, choices=GRADE, blank=True)


class JAMB(models.Model):
    applicant = models.OneToOneField(
        Application, on_delete=models.CASCADE, related_name="jamb"
    )
    year = models.IntegerField()
    score = models.IntegerField()

    def __str__(self):
        return str(self.score)
