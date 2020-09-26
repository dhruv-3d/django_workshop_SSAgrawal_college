from django.urls import path, include

from users import views


urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),    
    path("profile/<str:username>", views.profile, name="profile"),     
    path("accounts/", include("django.contrib.auth.urls")),
]
