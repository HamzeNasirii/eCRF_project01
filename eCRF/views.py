from django.views import generic

from .models import DemoInfo, HealthInfo, ContactInfoPhone, ContactInfoAddress


class PatientDemoInfoListView(generic.ListView):
    model = DemoInfo
    template_name = 'eCRF/demo_info.html'
    context_object_name = 'demo_info'
# Create your views here.


class PatientDetailView(generic.DetailView):
    model = HealthInfo
    template_name = 'eCRF/detail_patient_info.html'
    context_object_name = 'health_info'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["DemoInfo"] = DemoInfo.objects.all()
    #     context["HealthInfo"] = HealthInfo.objects.all()
    #     return context


 # class PatientCreateView(generic.CreateView):
 #     pass

