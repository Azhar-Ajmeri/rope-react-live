from django.db import models

# Create your models here.
class Column(models.Model):
    title = models.CharField(max_length=255, null=True, blank= True)
    order = models.IntegerField(null=False, blank= False, unique=True)

    def __str__(self):
        return str(self.title)

class Workpackage(models.Model):
    title= models.CharField(max_length=255, null=False, blank= False)
    procedure = models.CharField(max_length=255, default="", blank= True)

    date_of_creation = models.DateField(auto_now_add=True, blank= True)

    planned_start_date = models.DateField(auto_now_add=False, null=True, blank= True)
    planned_end_date = models.DateField(auto_now_add=False, null=True, blank= True)

    actual_start_date = models.DateField(auto_now_add=False, null=True, blank= True)
    actual_end_date = models.DateField(auto_now_add=False, null=True, blank= True)

    planned_efforts = models.IntegerField(null=True)
    actual_efforts = models.IntegerField(null=True)

    #Card Management
    project_lead_column = models.ForeignKey(Column, null=True, related_name='lead_column', on_delete=models.DO_NOTHING)
    project_team_column = models.ForeignKey(Column, null=True, related_name='team_column', on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.title)

    class Meta:
        order_with_respect_to = 'project_lead_column'

class UploadedDocuments(models.Model):
    file = models.FileField(blank=False, null=False)
    workpackage = models.ForeignKey(Workpackage, null=False, related_name='documents', on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)