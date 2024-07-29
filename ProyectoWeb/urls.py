from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('ProyectoWebApp.urls')),
    path('servicios/', include('ServicesApp.urls')),  
    path('blog/', include('blogApp.urls')),  
    path('contacto/', include('ContactApp.urls')),
    path('tienda/', include('TiendaApp.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
