from django.contrib import admin
from django.urls import path, include
from measurements import views
from rest_framework.routers import DefaultRouter

# TODO: настройте роутер и подключите `ProjectViewSet` и `MeasurementViewSet`
router = DefaultRouter()
router.register('project', views.ProjectViewSet, basename='project')
router.register('measurement', views.MeasurementViewSet, basename='measurement')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))

    # path('project/', views.ProjectViewSet.as_view(), name='project'),
    # path('measurement/', views.MeasurementViewSet, name='measurement')
]
