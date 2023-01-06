from django.urls import path, include
from . import views

urlpatterns = [
	path('index', views.index, name = 'Index'),
	path('reg_cia', views.reg_cia, name = 'Registracia'),
	path('company', views.company, name = 'company'),
	path('statistics', views.statistics, name = 'Statistics')
]