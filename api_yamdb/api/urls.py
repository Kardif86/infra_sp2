from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    MyTokenObtain,
    CategoryViewSet,
    GenreViewSet,
    TitleViewSet,
    RegisterView,
    UserViewSet,
    ReviewViewSet,
    CommentViewSet
)

app_name = 'api'

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'titles', TitleViewSet)
router.register(r'titles/(?P<title_id>\d+)/reviews',
                ReviewViewSet, basename='reviews')
router.register(r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)'
                r'/comments', CommentViewSet, basename='comments')
router.register(r'users', UserViewSet)
urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/token/', MyTokenObtain.as_view(),
         name='token_obtain_pair'),
    path(
        'v1/auth/signup/',
        RegisterView.as_view({'post': 'create', 'get': 'retrieve'}),
        name='signup'
    ),
]
