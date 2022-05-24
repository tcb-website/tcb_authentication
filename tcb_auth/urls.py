
from django.contrib import admin
from django.urls import path,include

admin.site.site_header = "The CodeBreakers Admin"
admin.site.site_title = "The CodeBreakers Admin Portal"
admin.site.index_title = "Welcome to The CodeBreakers Club Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
]