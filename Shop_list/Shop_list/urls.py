from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop_list/', include('sl_app.urls')),
    path('', RedirectView.as_view(url='/shop_list/', permanent=True)), # перенаправление сразу в приложение, на приветствие
    path('user/', include('sl_app.urls_user')),
]
