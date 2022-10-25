# from django.contrib.auth.models import User
from django.urls import include, path
from accounts.views import ProjectViewSet, RoleViewSet, TalentViewSet, CompanyViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('talents', TalentViewSet)
router.register('companies', CompanyViewSet)
router.register('roles', RoleViewSet)
router.register('projects', ProjectViewSet)
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]