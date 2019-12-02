from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from adminportal.views import LinkPageView
urlpatterns = [
    path('', auth_views.LoginView.as_view(
        template_name='adminportal/login.html')),
    # path('index/', HomePageView.as_view(), name="login"),
    path('register/', views.register, name="register"),
    path('links/', LinkPageView.as_view(), name="links"),
    path('admin/', admin.site.urls),
]
