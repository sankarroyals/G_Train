
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from api.views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (

    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include('api.urls'))
]
