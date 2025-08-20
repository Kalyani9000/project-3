from django.urls import path,include
import debug_toolbar
from . import views

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),

    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_event, name='register'),
]