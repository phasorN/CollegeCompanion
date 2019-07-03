from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Subject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    percentage = models.FloatField(blank=True, default=0)

    # color =  models.CharField(max_length = 200)
    # sub_type = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.title


class Period(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=False)
    time = models.TimeField(null=False)
    day = models.PositiveIntegerField(null=False)
    venue = models.CharField(max_length=200, default="---")
    period_number = models.PositiveIntegerField()

    def __str__(self):
        return self.subject.title + " " + str(self.day)


class Attendance(models.Model):
    period = models.ForeignKey(Period, on_delete=models.CASCADE, null=False)
    date = models.DateField(null=False)
    value_int = models.IntegerField(default=0, null=False)
    value_str = models.CharField(max_length=200, default="Not Marked")

    def __str__(self):
        return str(self.date) + " " + str(self.period.subject.title)
