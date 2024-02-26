from django.urls import path, include
from api.views import UserViewSet, DepartmentViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'department', DepartmentViewSet)
router.register(r'user', UserViewSet)


urlpatterns = [
    path('', include(router.urls))
]
