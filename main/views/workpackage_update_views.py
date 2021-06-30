from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import UpdateAPIView
from main.models import Workpackage, Column
from main.serializers import WorkpackageSerializer

# Create your views here.
class CreateWorkPackage(APIView):
    def put(self, request):
        data = request.data
        serializer = WorkpackageSerializer(data=data)
        serializer.is_valid()
        data = serializer.save()
        print(data)
        return Response(serializer.data)

class WorkPackageDetailsUpdate(APIView):
    def put(self, request):
        data = request.data
        workpackage = Workpackage.objects.get(id=data['id'])
        serializer = WorkpackageSerializer(workpackage, data, partial=True)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

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

