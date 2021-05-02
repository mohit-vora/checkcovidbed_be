from rest_framework.viewsets import ModelViewSet
# Create your views here.
from hospital.models import Hospital
from hospital.serializer import HospitalSerializer


class HospitalViewSet(ModelViewSet):
    http_method_names = ['post', 'get', 'delete']
    pagination_class = None
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
    permission_classes = ()
    authentication_classes = ()


