from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutUsPageView(TemplateView):
    template_name = 'pages/aboutus.html'


class ManageUserPageView(TemplateView):
    template_name = 'pages/manage_user.html'


class ElectronicCaseReportFormView(TemplateView):
    template_name = 'eCRF/eCRF_page.html'


class DemoInformationFormView(TemplateView):
    template_name = 'eCRF/demo_info.html'
# Create your views here.
