from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import BlogPost, BlogImage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ["username", "email", "password"]

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()  

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials.")

class BlogImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogImage
        fields = '__all__'

class BlogPostSerializer(serializers.ModelSerializer):
    images = BlogImageSerializer(many=True, read_only=True)
    is_published = serializers.BooleanField(read_only=True)

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'user', 'images', 'publish_at', 'is_published']
        
    def validate(self, data):
        if data["user"] != self.context["request"].user and self.context["request"].method in ["PUT", "DELETE"]:
            raise ValidationError("You have no permissions to edit this task")
        return data