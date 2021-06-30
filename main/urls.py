from django.urls import path
from .views import WorkpackageList, CreateWorkPackage, WorkPackageDetailsUpdate, UpdateWorkpackageColumn, UpdateWorkpackageOrder, ColumnList, DocumentUploadView, DocumentList

urlpatterns = [
    path('workpackages/', WorkpackageList.as_view()),
    path('columns/', ColumnList.as_view()),
    path('documents/', DocumentList.as_view()),

    path('workpackages-create/', CreateWorkPackage.as_view()),
    path('workpackages-update/', WorkPackageDetailsUpdate.as_view()),
    path('workpackages-column-update/', UpdateWorkpackageColumn.as_view()),
    path('workpackages-order-update/', UpdateWorkpackageOrder.as_view()),

    path('document-upload/', DocumentUploadView.as_view()),
]