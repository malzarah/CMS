from django.urls import path
#from . import views
from clients import views
from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
path('password/', views.change_password, name='change_password'),

]
