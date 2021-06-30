from rest_framework import serializers
from .models import Workpackage, Column, UploadedDocuments

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedDocuments
        fields = ['id','file', 'description', 'uploaded_at', 'workpackage']

class WorkpackageSerializer(serializers.ModelSerializer):
    documents = serializers.PrimaryKeyRelatedField(many=True, read_only=True)#DocumentSerializer(many=True)
    class Meta:
        model = Workpackage
        fields = '__all__'

class ColumnSerializer(serializers.ModelSerializer):
    lead_column = serializers.PrimaryKeyRelatedField(many=True, read_only=True)#WorkpackageSerializer(many=True)
    class Meta:
        model = Column
        fields = ['id', 'title', 'order', 'lead_column']
        