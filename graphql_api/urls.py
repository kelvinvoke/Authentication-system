"""graphql_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from my_app import views 
from django.contrib.auth import views as auth_views



#Wire up our API using automatic URL routing.
# Additionally, we include login URLS for the browsabe API.


urlpatterns = [
    path('', views.register, name ='register'),
    path('login/', views.loginPage , name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('admin/', admin.site.urls),

    path ('home/', views.Home, name= "home"),
    path('user/', views.userPage, name="user"),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='my_app/password_reset.html'), name='password_reset'),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name='my_app/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='my_app/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='my_app/password_reset_complete'), name='passowrd_reset_complete'),
    
]
