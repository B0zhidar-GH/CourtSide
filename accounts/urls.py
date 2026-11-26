import profile

from django.urls import path
#from courtside.urls import urlpatterns

from .views import RegisterView, AccountLogInView, AccountLogOutView, PlayerProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', AccountLogInView.as_view(), name='login'),
    path('logout/', AccountLogOutView.as_view(), name='logout'),
    path('profile/', PlayerProfileView.as_view(), name='profile')
]