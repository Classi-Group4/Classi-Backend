
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Classi.urls')),
    path('api/v1/',include('Classes.urls'))
]
