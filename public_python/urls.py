"""
URL configuration for public_python project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URL conf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("web.urls", namespace="web")),
    path("events/", include("events.urls", namespace="events")),
    path("friends/", include("friends.urls", namespace="friends")),
    path("blog/", include("blog.urls", namespace="blog")),
    path("about/", include("about.urls", namespace="about")),
    path("admin/", admin.site.urls),
]
