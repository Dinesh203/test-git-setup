from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="default_home_page"),
    path('home/', home, name="Home page"),
    path('show_about/', show_aobut_page),
    path('category/<int:cid>/', show_category_page),
    
    ]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)