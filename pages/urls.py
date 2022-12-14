from django.urls import path

from . import views

urlpatterns = [
    path('', views.LoginPageView.as_view(), name='login_page'),
    path('home/', views.HomePageView.as_view(), name='home'),
    path('aboutus/', views.AboutUsPageView.as_view(), name='aboutus'),
    path('manageuser/', views.ManageUserPageView.as_view(), name='manage_user'),
    path('report/', views.ElectronicCaseReportFormView.as_view(), name='eCRF'),
    path('demoinfo/', views.DemoInformationFormView.as_view(), name='demo_info'),
]
