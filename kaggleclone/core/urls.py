from django.contrib import admin
from django.urls import path
from  .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.current_datetime,name='current_datetime'),
    path('',views.home, name='home')
]
