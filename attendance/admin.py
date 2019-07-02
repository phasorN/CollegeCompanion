from django.contrib import admin
from attendance import models


# Register your models here.
admin.site.register(models.Subject)
admin.site.register(models.Period)
admin.site.register(models.Attendance)
