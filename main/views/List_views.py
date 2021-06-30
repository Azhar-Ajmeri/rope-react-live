from rest_framework.generics import ListCreateAPIView
from main.models import Workpackage, Column, UploadedDocuments
from main.serializers import WorkpackageSerializer, ColumnSerializer, DocumentSerializer

# Create your views here.
class WorkpackageList(ListCreateAPIView):
    queryset = Workpackage.objects.all()
    serializer_class = WorkpackageSerializer

class ColumnList(ListCreateAPIView):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer

class DocumentList(ListCreateAPIView):
    queryset = UploadedDocuments.objects.all()
    serializer_class = DocumentSerializer