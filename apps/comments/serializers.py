from rest_framework import serializers

from .models import Comment


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CommentSerializer(serializers.ModelSerializer):
    reply_set = RecursiveSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'post_id', 'user_id', 'message', 'parent_id', 'created_at', 'reply_set', 'status')
