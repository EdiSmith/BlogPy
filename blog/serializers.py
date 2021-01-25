from rest_framework import serializers

class SingleArticleSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, allow_blank=False, allow_null=False, max_length=128)
    cover = serializers.CharField(required=True, allow_blank=False, allow_null=False, max_length=256)
    body = serializers.CharField(required=True, allow_blank=False, allow_null=False, max_length=2646)
    created_at = serializers.DateTimeField(required=True, allow_null=False)