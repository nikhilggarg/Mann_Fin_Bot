from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
	path('home', views.homepage, name = 'homepage'),
	path('save_message/',views.savemessage, name='same_messs'),
	path('',views.login,name='login'),
	path('registration/',views.registration,name='registration'),
	path('userlogout/',views.userlogout,name="userlogout"),
	path('chart/',views.chart, name="chart"),
	# ... Other urlpatterns as they were ...

path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'), 
path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),
     {'template_name': "registration/password_reset_done.html"}, name='password_reset_done'),
path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),
     {'template_name': "registration/password_reset_complete.html"}, name='password_reset_complete'),    
]