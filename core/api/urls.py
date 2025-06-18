from django.urls import path
from core.api import views

urlpatterns = [
    path('user-create/', views.UserCreateAPIView.as_view()),
    path('wishlist-create/', views.WishlistCreateAPIView.as_view()),
    path('user-wishlist-list/', views.UserWishlistListAPIView.as_view()),
    path('settings/', views.SiteSettingsListAPIView.as_view())
]