from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render


from .models import DemoInfo, HealthInfo, ContactInfoPhone, ContactInfoAddress
# from .form import DemoForm


class PatientDemoInfoListView(generic.ListView):
    model = DemoInfo
    template_name = 'eCRF/demo_list_view.html'
    context_object_name = 'demo_info'


class PatientDetailView(generic.DetailView):
    model = DemoInfo
    template_name = 'eCRF/detail_patient_info.html'
    # context_object_name = 'demo_info'

    def get_context_data(self, **kwargs):
        context = super(PatientDetailView, self).get_context_data(**kwargs)
        patient = DemoInfo.objects.get(pk=self.kwargs['pk'])
        context['demo'] = DemoInfo.objects.all().filter(national_code=patient)
        context['health'] = HealthInfo.objects.all().filter(national_code=patient)
        context['address'] = ContactInfoAddress.objects.all().filter(national_code=patient)
        context['phone'] = ContactInfoPhone.objects.all().filter(national_code=patient)
        # context['festival_list'] = Festival.objects.all()
        # And so on for more models
        return context


class DemoInfoCreateView(generic.CreateView):
    model = DemoInfo
    fields = ['first_name', 'last_name', 'national_code', 'gender', 'birthday', 'educate_rate', 'economic_situation',
              'status_job']
    template_name = 'eCRF/patient_register.html'
    success_url = reverse_lazy('patient_list')
    # success_url = ''
# class IndexView(ListView):
# context_object_name = 'home_list'
# template_name = 'contacts/index.html'
# queryset = Individual.objects.all()
#
# def get_context_data(self, **kwargs):
#     context = super(IndexView, self).get_context_data(**kwargs)
#     context['roles'] = Role.objects.all()
#     context['venue_list'] = Venue.objects.all()
#     context['festival_list'] = Festival.objects.all()
#     # And so on for more models
#     return context


class DemoInfoUpdateView(generic.UpdateView):
    model = DemoInfo
    fields = ['first_name', 'last_name', 'national_code', 'gender', 'birthday', 'educate_rate', 'economic_situation',
              'status_job']
    template_name = 'eCRF/patient_update.html'


class DemoInfoDeleteView(generic.DeleteView):
    model = DemoInfo
    fields = ['first_name', 'last_name', 'national_code', 'gender', 'birthday', 'educate_rate', 'economic_situation',
              'status_job']
    template_name = 'eCRF/patient_delete.html'

    # def get_success_url(self):

# class PatientCreateView(generic.CreateView):
#     model = DemoInfo
#     form_class = DemoForm
#     # template_name = 'eCRF/patient_register.html'
#     # context_object_name = 'Register'
#
#     def form_valid(self, form):
#         obj = form.save(commit=False)
#         obj.national_code = self.request.user
#
#         patient_id = int(self.kwargs['demo_info_id'])
#         patient = get_object_or_404(DemoInfo, id=patient_id)
#         obj.patient = patient
#
#         return super().form_valid(form)


# class PatientAddressDetailView(generic.DetailView):
#     model = ContactInfoAddress
#     template_name = 'eCRF/detail_patient_info.html'
#     context_object_name = 'address_info'
#
#
# class PatientPhoneDetailView(generic.DetailView):
#     model = ContactInfoPhone
#     template_name = 'eCRF/detail_patient_info.html'
#     context_object_name = 'phone_info'
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["DemoInfo"] = DemoInfo.objects.all()
    #     context["HealthInfo"] = HealthInfo.objects.all()
    #     return context


