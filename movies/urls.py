# urls.py (myappディレクトリ内に新しく作成)
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet

router = DefaultRouter()
router.register('movies', MovieViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # 明示的なエンドポイントの追加
    path('movies/', MovieViewSet.as_view({'get': 'list', 'post': 'create'}), name='movie-list-create'),
    path('movies/<int:pk>/', MovieViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='movie-detail'),
    # 新しい検索エンドポイント
    path('movies/search/', MovieViewSet.as_view({'get': 'list'}), name='movie-search'),
]