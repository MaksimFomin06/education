from django.contrib import admin
from django.urls import path
from webapp.views import get_config_form

urlpatterns = [
    path('admin/', admin.site.urls),
    path('config-form', get_config_form, name="get-config-form")
]
