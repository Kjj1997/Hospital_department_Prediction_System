from django.views.generic import TemplateView

from . import views
from django.urls import path,include
from .views import VisitReasonViewSet
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register(r'patient_info',VisitReasonViewSet)


urlpatterns = [
    path('', views.home, name='home'),  # Homepage
    path('visit_reason/', views.visit_reason, name='visit_reason'),
    path('',include(router.urls)),
    path('home/', views.home_redirect, name='home-api'),
    path('predict_department/<str:reason_text>/',views.predict_department_api,name='predict_department_api')
]

