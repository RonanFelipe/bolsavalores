from django.conf.urls import url
from django.urls import include

from rest_framework.routers import DefaultRouter

from bolsa import views

# http://127.0.0.1:8000/api/v1/ativos/
router = DefaultRouter()
router.register(r'ativos', views.AtivoSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
