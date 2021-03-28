from django.contrib import admin
from django.urls import path, include
from authapp import views

#added to change the admin page stuff
admin.site.site_header = "Harry Ice Cream Admin"
admin.site.site_title = "Harry Ice Cream Admin Portal"
admin.site.index_title = "Welcome to Harry Ice Creams"
#added to change the admin page stuff


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authapp.urls'))
]
