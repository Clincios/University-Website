from . import views
from django.urls import path
from django.contrib.auth import logout
from .views import SignUpView, CustomLoginView, DashboardView, CustomPasswordResetView,CustomPasswordResetConfirmView,PasswordResetCompleteView

app_name='wgis'

urlpatterns = [
    # Authentication URLs
    path("",views.home, name="home"),
    path('base/',views.base, name="base"),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('password-reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='reset_password'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('verify-email/<uuid:token>/', views.verify_email, name='verify_email'),

    path('auth/google/login/', views.google_login, name='google_login'),
    path('auth/google/callback/', views.google_callback, name='google_callback'),

    path('about/', views.about, name='about'),
    path('academics/', views.academics, name='academics'),
    path('admissions/', views.admissions, name='admissions'),

    path('staff/', views.staff, name='staff'),
    path('students/', views.students, name='students'),

    path('more/', views.more, name='more'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
]