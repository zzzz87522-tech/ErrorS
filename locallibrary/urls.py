"""
URL configuration for locallibrary project.
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('', RedirectView.as_view(url='/catalog/'), name='home'),
]

# Аутентификация Django: login, logout, смена пароля и т. д.
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
