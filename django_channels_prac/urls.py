from django.contrib import admin
from django.urls import path, include
from user.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),
    path('', Index.as_view()),
]
