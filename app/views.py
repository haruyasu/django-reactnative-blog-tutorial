from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import BlogSerializer
from .models import Blog


# ブログ一覧
class BlogListView(ListAPIView):
    queryset = Blog.objects.order_by('-created_at')
    serializer_class = BlogSerializer


# ブログ詳細
class BlogDetailView(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
