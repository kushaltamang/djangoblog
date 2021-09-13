from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views # for login logout auth
from django.conf import settings
from django.conf.urls.static import static

# this is where Django searches for path when user goes to the webpage
# add route to our website eg: localhost:8000/admin
# /blog maps to blog.urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'), # user-registration page
    #path('blog/', include('blog.urls')), # chops 'blog/' and sends remaining string to blog.urls path when user goes to the homepage
    path('', include('blog.urls')), # sends empty string to blogs.urls
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'), # handles login logic and forms, but doesnt create the template
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'), # template needed to be created at users/logout.html
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'), # reset user pwd
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'), # after password reset submitted successfully, go to this route
    path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'), # password reset confirm route
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'), # complete reseting pwd
    path('profile/', user_views.profile, name='profile'),  
]

#only add in debug mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   



