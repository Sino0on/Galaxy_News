from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('News/', PostListView.as_view()),
    path('News/create', PostCreateView.as_view()),
    path('News/update/<int:pk>', PostUpdateView.as_view()),
    path('register/', RegisterView.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
