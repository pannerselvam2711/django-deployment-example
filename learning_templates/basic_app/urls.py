from django.urls import path

# from django.conf.urls import include

from basic_app import views

# Template Tagging
app_name = "basic_app"

urlpatterns = [
    path("relative", views.relative, name="relative"),
    path("other", views.other, name="other"),
]

"""
for reference:
from other url.py

from django.contrib import admin
from django.urls import path

from basic_app import views

from django.conf.urls import include

urlpatterns = [
    path("", views.index, name="index"),
    path("admin/", admin.site.urls),
    path("basic_app/", include("basic_app.urls")),
]

"""
