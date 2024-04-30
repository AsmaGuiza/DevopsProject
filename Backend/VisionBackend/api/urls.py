from django.urls import path,include
from .views import AIModelListView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('models',AIModelListView)

urlpatterns = [
    path('', include(router.urls)),
]