from django.contrib import admin
from django.urls import path, include
from .views import homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('quiz/', include('quiz.urls')),
    path('accounts/', include('accounts.urls', 'accounts')),
    path('', homepage)
]
