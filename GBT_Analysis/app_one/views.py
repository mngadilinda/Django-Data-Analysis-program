from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

class ReportView(TemplateView):
    template_name = 'report.html'

class AnalysisView(TemplateView):
    template_name = 'analysis.html'

class AboutView(TemplateView):
    template_name = 'about.html'