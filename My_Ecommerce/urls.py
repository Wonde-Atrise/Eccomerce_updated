
from django.contrib import admin
from django.urls import path, include
from Ecommerce_main import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
      path('', views.Index,name='home'),
    path('mains/', include('Ecommerce_main.url')),
    path('User-manage/', include('Profile.url')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
