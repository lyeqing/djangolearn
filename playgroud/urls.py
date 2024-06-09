from django.urls import path
from . import views
from django.urls import path, include
from rest_framework import routers
from playgroud import views

router = routers.DefaultRouter()
router.register(r'person', views.PersonViewSet)
router.register(r'activities', views.ActivityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]