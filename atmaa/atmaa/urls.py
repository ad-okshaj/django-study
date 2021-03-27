from django.contrib import admin
from django.urls import path, include
from authapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authapp.urls'))
]
