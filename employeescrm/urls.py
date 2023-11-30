"""
URL configuration for employeescrm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crm import views
from django.conf import settings
from django.conf.urls.static import static
# http://localhost:8000/employees/2 =kwargs={"pk":6}

urlpatterns = [
    path('admin/', admin.site.urls),
    path("employees/add",views.EmployeesCreateView.as_view(),name="emp-add"),
    path("employees/all",views.EmployeesListView.as_view(),name="emp-all"),
    path("employees/<int:pk>",views.EmployeeeDetailView.as_view(),name="emp-details"),
    path("employees/<int:pk>/remove",views.EmployeeeDetailView.as_view(),name="emp-delete"),
    path("employees/<int:pk>/change/",views.EmployeesUpdateView.as_view(),name="emp-edit"),
    path("signup",views.SignUpView.as_view(),name="register"),
    path("",views.SignInView.as_view(),name="signin"),
    path("signout",views.SignOutView.as_view(),name="signout")

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
