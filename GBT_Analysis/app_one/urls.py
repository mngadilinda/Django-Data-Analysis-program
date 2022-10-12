from django.urls import path
from app_one import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('report/', views.ReportView.as_view(), name='report'),
    path('analysis/', views.AnalysisView.as_view(), name='analysis'),
    path('about/', views.AboutView.as_view(), name='about'),
]
