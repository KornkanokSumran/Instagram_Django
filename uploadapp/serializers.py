from rest_framework import serializers
from .models import File, Description, Comment

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"

class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

