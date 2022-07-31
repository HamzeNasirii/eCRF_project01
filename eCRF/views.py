from django.shortcuts import render
from django.views.generic import TemplateView


class ElectronicCaseReportFormView(TemplateView):
    template_name = 'eCRF/eCRF_page.html'


class DemoInformationFormView(TemplateView):
    template_name = 'eCRF/demo_info.html'
# Create your views here.
