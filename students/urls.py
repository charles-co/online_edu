from django.conf.urls import url
from django.urls import path
from django.views.decorators.cache import cache_page
from students.views import StudentRegistrationFormView, StudentEnrollCourseView, StudentCourseDetailView, StudentCourseListView

urlpatterns = [
    path('register/', StudentRegistrationFormView.as_view(), name='student_registration'),
    path('enroll-course/', StudentEnrollCourseView.as_view(), name='student_enroll_course'),
    path('courses/', StudentCourseListView.as_view(), name='student_course_list'),
    path('course/<int:pk>/', cache_page(60 * 15)(StudentCourseDetailView.as_view()), name='student_course_detail'),
    path('course/<int:pk>/<int:module_id>/', cache_page(60 * 15)(StudentCourseDetailView.as_view()), name='student_course_detail_module'),


]
