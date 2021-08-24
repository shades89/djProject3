from django.contrib import admin
from django.urls import path, include
admin.site.site_header = "Deb Ice Cream Admin"
admin.site.site_title = "Deb Ice Cream Admin Portal"
admin.site.index_title = "Welcome to Deb Ice Cream Researcher Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'))
]

