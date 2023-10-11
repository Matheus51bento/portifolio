from django.urls import path
from core.views import IndexView, ProjectDetail, ContactCreateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('projeto/<int:pk>', ProjectDetail.as_view(), name="detail_project"),
    path('Contato', ContactCreateView.as_view(), name="contato_view"),
]
