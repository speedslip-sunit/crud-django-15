"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
import employee.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', employee.views.echo, name="echo"),
    path('api/department/add', employee.views.department_create, name="department_create"),
    path('api/department/list', employee.views.department_list, name="department_list"),
    path('api/department/interact/<uuid:department_id>', employee.views.department_interact, name="department_interact"),

    path('api/employee/add', employee.views.employee_create, name="employee_create"),
    path('api/employee/interact/<uuid:employee_id>', employee.views.employee_interact, name="employee_interact"),
    path('api/employee/list', employee.views.employee_list, name="employee_list"),
]
