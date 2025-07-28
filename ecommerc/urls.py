
from django.contrib import admin
from django.urls import path
from apps.views import my_view,product
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', my_view),
    path('product/', product),
      
]
