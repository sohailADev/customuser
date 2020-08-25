
from django.urls import path
from customuser_app import views
urlpatterns = [
    path('',views.index_view,name='home_page' ),
    path('login/',views.login_view, name='login_page' ),
    path('signup/',views.signup_view,name='signup_page' ),
    path('logout/',views.logout_view,name='logout_page' ),
   
]
