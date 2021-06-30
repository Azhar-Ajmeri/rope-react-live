from django.urls import path
from .views import RegisterView, UpdateView, UserDetailsView, CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('register/', RegisterView.as_view()),
    path('user-details/', UserDetailsView.as_view()),
    path('update/', UpdateView.as_view()),
]