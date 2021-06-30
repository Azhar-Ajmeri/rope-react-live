from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import UserSerializer, UserSerializerWithTokens, CustomTokenObtainPairViewSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairViewSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        serializer = UserSerializerWithTokens(user, many=False)
        return Response(serializer.data)

class UpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def put(self, request):
        user = request.user
        data = {k: v for k, v in request.data.items() if v is not ""}
        serializer = UserSerializer(user, data = data, partial=True)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        serializer = UserSerializerWithTokens(user, many=False)
        return Response(serializer.data)

class UserDetailsView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)
        

