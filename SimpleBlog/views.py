from django.contrib.auth import login, authenticate, logout
from rest_framework import generics, permissions, status, viewsets
from rest_framework.pagination import PageNumberPagination
from .models import BlogPost, BlogImage
from .serializers import BlogPostSerializer, UserCreateSerializer, UserLoginSerializer, BlogImageSerializer
from django.contrib.auth.models import User
from .custom_exceptions import CustomAPIException, ExceptionType
from rest_framework.response import Response



class BlogImageViewSet(viewsets.ModelViewSet):
    queryset = BlogImage.objects.all()
    serializer_class = BlogImageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BlogPostList(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all().order_by('-publish_at')
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = PageNumberPagination

class BlogPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.AllowAny]

class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        login(request, user)
        return Response({"detail": "Login Successful"})

class LogoutView(generics.GenericAPIView):
    def get(self, request):
        logout(request)
        return Response({"detail" : "Logout Successful"}, status=204)