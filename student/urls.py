from django.urls import path, include
from rest_framework import routers
from .views import (RegisterView, LoginView, 
                    ProfileView,ProfileUpdateView,
                    PaswordChangeView,SendResetPasswordView,
                    ResetPasswordView,MyCoureseView)

router =routers.DefaultRouter()
router.register(r'edit', ProfileUpdateView, basename='edit')
router.register(r'mycours',MyCoureseView, basename='mycourse')

urlpatterns = [
    path('',include(router.urls)),
    path('register/',RegisterView.as_view()),
    path('login/',LoginView.as_view()),
    path('profile/',ProfileView.as_view()),
    path('change/',PaswordChangeView.as_view()),
    path('send-password/',SendResetPasswordView.as_view()),
    path('reset-password/<uid>/<token>/',ResetPasswordView.as_view()),
    # path('edit/<slug:slug>/',ProfileUpdateView.as_view()),
]

