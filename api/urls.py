from django.urls import path
from api import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("v2/employees",views.EmployeeViewsetView,basename="employees")

urlpatterns=[

    path('employees/',views.EmployeeListCreateView.as_view()),
    path('employees/<int:pk>/',views.EmpolyeeMixinView.as_view())

]+router.urls