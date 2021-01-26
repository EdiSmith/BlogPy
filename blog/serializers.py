from rest_framework import serializers

class SingleArticleSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, allow_blank=False, allow_null=False, max_length=128)
    cover = serializers.CharField(required=True, allow_blank=False, allow_null=False, max_length=256)
    body = serializers.CharField(required=True, allow_blank=False, allow_null=False, max_length=2646)
    created_at = serializers.DateTimeField(required=True, allow_null=False)


class SubmitArticleSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, allow_blank=False, allow_null=False, max_length=128)
    cover = serializers.FileField(required=True, allow_null=False, allow_empty_file=False)
    body = serializers.CharField(required=True, allow_blank=False, allow_null=False, max_length=2646)
    category_id = serializers.IntegerField(required=True, allow_null=False)
    author_id = serializers.IntegerField(required=True, allow_null=False)
    promote = serializers.BooleanField(required=True, allow_null=False)
