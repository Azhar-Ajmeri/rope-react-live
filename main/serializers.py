from rest_framework import serializers
from .models import Workpackage, Column, UploadedDocuments

class DocumentSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField()
    class Meta:
        model = UploadedDocuments
        fields = ['id', 'file', 'file_url', 'description', 'uploaded_at', 'workpackage']

    def get_file_url(self, obj):
        request = self.context.get('request')
        file_url = obj.file.url
        return request.build_absolute_uri(file_url)

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
        