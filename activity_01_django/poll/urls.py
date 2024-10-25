from django.urls import path
from enquete.views import index

urlpatterns = [
    path('', index, name='index_enquete')
]