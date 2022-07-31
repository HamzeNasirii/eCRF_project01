from django.urls import path
from .views import ElectronicCRFListView, PatientDetailView

urlpatterns = [
    path('', ElectronicCRFListView.as_view(), name='patient_list'),
    path('<int:pk>/', PatientDetailView.as_view, name='patient_detail_view'),
]
