from rest_framework import routers
from .views import PublishViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'publish', PublishViewSet, 'publish')

# router = routers.SimpleRouter()
# router.register(r'publish', PublishViewSet)
# # router.register(r'accounts', AccountViewSet)

urlpatterns = [
    path('api/docs/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]