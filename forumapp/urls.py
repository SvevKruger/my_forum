from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, TopicViewSet, PostViewSet, CommentViewSet, UserRegistrationView, CustomLoginView, CustomLogoutView

router = DefaultRouter()

router.register(r'user', UserProfileViewSet, basename='user')
router.register(r'topic', TopicViewSet, basename='topic')
router.register(r'post', PostViewSet, basename='post')
router.register(r'comment', CommentViewSet, basename='comment')


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', CustomLoginView.as_view(), name='custom-login'),
    path('logout/', CustomLogoutView.as_view(), name='custom-logout'),
    path('', include(router.urls)),
]
