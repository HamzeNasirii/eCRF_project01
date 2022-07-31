from django.contrib import admin

from .models import DemoInfo, HealthInfo


@admin.register(DemoInfo)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['national_code', 'first_name', 'last_name', ]
# Register your models here.
