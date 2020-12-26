from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import Hello, HelloViewSets, UserProfileViewSet

router = DefaultRouter()
router.register('hello', HelloViewSets, base_name='hello')
router.register('profile', UserProfileViewSet)

urlpatterns = [
    path('a/', Hello.as_view() ,name="hello"),
    path('', include(router.urls))
]