"""SEAS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from users import views as 

from seasapp import populations,views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',populations.upload_file),
    path('success/',views.success),
    path('classroom/',views.classroom),
    path('classroomTable/',views.classroom_requirement),
    path('resource_usage/',views.resource_usage),
    path('available_resource/',views.available_resource),
    path('availability_course_offering/',views.Availability_course_offering_comparison),
    path('enrollment_wise_course_distribution/',views.Enrollment_wise_course_distribution)
]
