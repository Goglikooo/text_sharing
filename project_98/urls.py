from django.contrib import admin
from django.urls import path
from text_sharing import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='index'),
    path('shared/<str:sha>', views.share_text),
    path('edit/<str:sha>', views.edit_text, name='edit'),
]
