from django.contrib import admin
from django.urls import path
from .views import HomePageView,AboutPageView,SnacksPageView,SnackDetailPageView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomePageView.as_view(),name='home'),
    path('about/', AboutPageView.as_view(),name='about'),
    path('snacks/',SnacksPageView.as_view(),name='snacks'),
    path('<int:pk>/',SnackDetailPageView.as_view(),name="snack_detail")
]