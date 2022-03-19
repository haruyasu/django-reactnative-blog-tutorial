from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.BlogListView.as_view()),
    path('blog/<str:pk>/', views.BlogDetailView.as_view()),
]
