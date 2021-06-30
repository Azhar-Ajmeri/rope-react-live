from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Workpackage, Column
from .serializers import WorkpackageSerializer, ColumnSerializer

# Create your views here.
class WorkpackageList(ListCreateAPIView):
    queryset = Workpackage.objects.all()
    serializer_class = WorkpackageSerializer

class ColumnList(ListCreateAPIView):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer

class UpdateWorkpackageColumn(APIView):
    def put(self, request):
        data = request.data
        columnId = data["columnId"]
        workpackageId = data["workpackageId"]
        order = data["order"]
        obj = Workpackage.objects.get(id=workpackageId)
        obj.project_lead_column = Column.objects.get(id=columnId)
        obj.save()
        column = Column.objects.get(id=columnId)
        column.set_workpackage_order(order)
        return Response({"status" : True})
    
class UpdateWorkpackageOrder(APIView):
    def put(self, request):
        data = request.data
        columnId = data["columnId"]
        order = data["order"]
        column = Column.objects.get(id=columnId)
        column.set_workpackage_order(order)
        return Response({"status" : True})

