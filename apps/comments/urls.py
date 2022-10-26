from django.urls import path, include
from rest_framework import routers

from . import views

app_name = 'comments'

apiRouter = routers.DefaultRouter()

apiRouter.register(r'comments', views.CommentViewSet)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('comments/', views.CommentListAPIView.as_view(), name='comments'),
    path('api/', include(apiRouter.urls)),
]
