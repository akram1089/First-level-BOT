from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('login', views.login_page, name='login_page'),
    path('signup', views.signup_page, name='signup_page'),
    path('user_signUp', views.user_signUp, name='user_signUp'),
    path('verify_otp', views.verify_otp, name='verify_otp'),
    path('resend_user_signup', views.resend_user_signup, name='resend_user_signup'),
    path('login_user', views.login_user, name='login_user'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('', views.landing_page, name='landing_page'),
    path('add_broker_api_main', views.add_broker_api_main, name='add_broker_api_main'),
    path('check_user_logged_in', views.check_user_logged_in, name='check_user_logged_in'),
    path('delete_broker', views.delete_broker, name='delete_broker'),
    path('verify_active_api', views.verify_active_api, name='verify_active_api'),
    path('verify_otp_api_activation', views.verify_otp_api_activation, name='verify_otp_api_activation'),
    path('update_active_api', views.update_active_api, name='update_active_api'),
    path('broker_details', views.broker_details, name='broker_details'),
    path('get_api_config_data', views.get_api_config_data, name='get_api_config_data'),

]