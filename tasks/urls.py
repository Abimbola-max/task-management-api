from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, RegisterView, login_view
from django.urls import path

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', login_view, name='login'),
]
urlpatterns += router.urls
