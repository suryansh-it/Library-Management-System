#Use a router to automatically generate RESTful URLs.

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet, BorrowerViewSet


router = DefaultRouter()
router.register(r'authors' , AuthorViewSet)
router.register(r'books', BookViewSet)
router.register(r'borrowers' , BorrowerViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]