from django.urls import path, include
from django.contrib import admin
from core import views as core_views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
    path('core/',include('core.urls')),
    path('api-token-auth/', obtain_auth_token), #This gives us access to token authentication
    path('carpark/', include('carparkAPI.urls')),
]