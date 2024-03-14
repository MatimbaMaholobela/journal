
from django.contrib import admin
from django.urls import path
from testing import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name="testPage"),
    path("journal/",views.journal,name="journal"),
]
