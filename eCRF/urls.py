from django.urls import path
from .views import PatientDemoInfoListView, PatientDetailView

urlpatterns = [
    path('patientlist/', PatientDemoInfoListView.as_view(), name='patient_list'),
    path('<int:pk>/', PatientDetailView.as_view(), name='patient_detail'),
]
