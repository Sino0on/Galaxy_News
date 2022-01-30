from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    # path('media/Photos/<int:Y>/<int:m>/<int:d>/<str:name>', show_img)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
