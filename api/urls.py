from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.accounts.views import OrganizationViewSet

router = DefaultRouter()

router.register('organizations', OrganizationViewSet, 'organizations')

urlpatterns = [
    path('v1/', include(router.urls))
]
