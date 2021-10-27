from django.urls import path
#from . import views
from . import views
from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile_update/', views.profile_update, name='profile_update'),
]

