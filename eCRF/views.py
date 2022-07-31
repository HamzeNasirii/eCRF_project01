from django.views import generic

from .models import DemoInfo, HealthInfo, ContactInfoPhone, ContactInfoAddress


class ElectronicCRFListView(generic.ListView):
    model = DemoInfo
    template_name = 'eCRF/demo_info.html'
    context_object_name = 'demo_info'
# Create your views here.


class PatientDetailView(generic.DetailView):
    model = DemoInfo, HealthInfo, ContactInfoPhone, ContactInfoAddress
    template_name = 'eCRF/detail_patient_info.html'
    context_object_name = 'demo_info'


 # class PatientCreateView(generic.CreateView):
 #     pass

