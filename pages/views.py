from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutUsPageView(TemplateView):
    template_name = 'pages/aboutus.html'


class ManageUserPageView(TemplateView):
    template_name = 'pages/manage_user.html'

# Create your views here.
