from django.urls import path

from . import views

urlpatterns = [
    path('report/', views.ElectronicCaseReportFormView.as_view(), name='eCRF'),
    path('demoinfo/', views.DemoInformationFormView.as_view(), name='demo_info'),
]
