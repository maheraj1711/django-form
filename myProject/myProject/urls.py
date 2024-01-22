from django.contrib import admin
from django.urls import path, include # 👈 1. Add this line

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myApp.urls'))
]