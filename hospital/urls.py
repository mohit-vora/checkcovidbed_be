from django.conf.urls import include, url
from rest_framework.routers import SimpleRouter
from .views import HospitalViewSet

app_name = 'hospital'

router = SimpleRouter()
router.register(r'', HospitalViewSet, basename='hospitals')

urlpatterns = [
    url(r'', include(router.urls)),
]

