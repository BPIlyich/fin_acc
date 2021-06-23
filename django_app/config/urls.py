from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', login_required(TemplateView.as_view(
        template_name='home.html')), name='home'),
    path('users/', include('users.urls')),
]