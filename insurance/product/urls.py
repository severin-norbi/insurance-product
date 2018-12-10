from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('risktype', views.RiskTypeViewSet)
router.register('risktypefield', views.RiskTypeFieldViewSet)
router.register('enumoption', views.EnumOptionViewSet)

urlpatterns = [
#    path('', views.index, name='index'),
    path('api/', include(router.urls)),
]
