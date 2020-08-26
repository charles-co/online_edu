from django.urls import path, include
from .views import SubjectListView, CourseViewSet, SubjectDetailView, CourseEnrollView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('courses', CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('subjects/', SubjectListView.as_view(), name='subject_list'),
    path('subjects/<int:pk>/', SubjectDetailView.as_view(), name='subject_detail'),
    path('courses/<int:pk>/enroll/', CourseEnrollView.as_view(), name='course_enroll'),
]
