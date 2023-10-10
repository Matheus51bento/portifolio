from django.urls import path
from core.views import IndexView, ProjectDetail

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('projeto/<int:pk>', ProjectDetail.as_view(), name="detail_project"),
]
