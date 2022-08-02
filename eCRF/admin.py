from django.contrib import admin

from .models import DemoInfo, HealthInfo, ContactInfoAddress, ContactInfoPhone


@admin.register(DemoInfo)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['national_code', 'first_name', 'last_name', ]


@admin.register(HealthInfo)
class PatientHealth(admin.ModelAdmin):
    list_display = ['age', 'weight', 'height', 'BMI', 'pregnancy_status', 'breast_feeding_status', 'smoking', ]


@admin.register(ContactInfoAddress)
class PatientAddress(admin.ModelAdmin):
    list_display = ['country', 'province', 'town', 'village', 'post_code', ]


@admin.register(ContactInfoPhone)
class PatientPhone(admin.ModelAdmin):
    list_display = ['home_phone', 'cell_phone', 'fax', 'work_phone', 'cellular_phone', 'health_care_proxy_phone', 'emergency_phone', ]

