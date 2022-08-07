from django.urls import path
from .views import (
    PatientDemoInfoListView,
    PatientDetailView,
    DemoInfoCreateView,
    DemoInfoUpdateView,
    DemoInfoDeleteView
)

urlpatterns = [
    path('patientlist/', PatientDemoInfoListView.as_view(), name='patient_list'),  # نمایش لیست بیماران ثبتنام شده
    path('<int:pk>/delete/', DemoInfoDeleteView.as_view(), name='patient_delete'),  # حذف بیمار ثبتنام شده
    path('<int:pk>/edit/', DemoInfoUpdateView.as_view(), name='patient_update'),  # ویرایش بیمار ثبتنام شده
    path('ptntcrtviw/', DemoInfoCreateView.as_view(), name='patient_create'),  # ثبتان بیمار جدید
    path('<int:pk>/', PatientDetailView.as_view(), name='patient_detail'),
    # path('register/<int:demo_info_id>/', PatientCreateView.as_view(), name='ptntCrtVw'),
]
