from django.urls import path, include
from .views import LoginView, SignUpView, UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('signup/', SignUpView),
    path('login/', LoginView),
]

urlpatterns += router.urls
