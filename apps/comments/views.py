from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.comments.models import Comment
from apps.comments.serializers import CommentSerializer


class CommentListAPIView(ListCreateAPIView):
    queryset = Comment.objects.filter(status=True)
    serializer_class = CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    @action(detail=False)
    def roots(self, request):
        queryset = Comment.objects.filter(parent=None)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
