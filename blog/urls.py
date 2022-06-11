from django.urls import path
from . import views
urlpatterns = [
    path('', views.Time_Table, name='Time_Table'),
    path('VIOL', views.VIOL, name='VIOL')
]