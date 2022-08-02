from django.contrib import admin

from .models import DemoInfo, HealthInfo


@admin.register(DemoInfo)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['national_code', 'first_name', 'last_name', ]


@admin.register(HealthInfo)
class PatientHealth(admin.ModelAdmin):
    list_display = ['age', 'weight', 'height', 'BMI', 'pregnancy_status', 'breast_feeding_status', 'smoking', ]
# Register your models here.
