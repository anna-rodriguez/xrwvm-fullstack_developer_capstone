# Uncomment the imports before you add the code
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.views.generic import TemplateView

app_name = 'djangoapp'
urlpatterns = [
    # # path for registration
    path('register', views.registration, name='register'),   # API 
    path('register/', TemplateView.as_view(template_name="index.html")),  
    
    # path for login
    path(route='login', view=views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    # path for dealer reviews view

    # path for add a review view
    path(route='get_cars', view=views.get_cars, name ='getcars'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
