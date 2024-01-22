from django.urls import path
from django.contrib import admin
from .views import ( signup,signin,UserDetailsView,AppointmentListView,AppointmentDetailView)
from rest_framework.authtoken.views import obtain_auth_token
from . import views
app_name = 'doctdrive_app'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('users/<int:pk>/', UserDetailsView.as_view(), name='user-details'),
    path('api/token-auth/', obtain_auth_token, name='api-token-auth'),
    path('doctdrive_app/api/appointments/', AppointmentListView.as_view(), name='appointments_api'),
    path('doctdrive_app/api/appointments/<int:pk>/', AppointmentDetailView.as_view(), name='appointment_detail_api'),
    path('doctdrive_app/api/appointments/create/', views.create_appointment, name='create_appointment'),
    # path('doctdrive_app/api/appointments/<int:pk>/update/', views.update_appointment, name='update_appointment'),
    #path('doctdrive_app/api/appointments/<int:pk>/update/', views.update_appointment, name='update_appointment'),
    path('doctdrive_app/api/appointments/<int:pk>/delete/', views.delete_appointment, name='delete_appointment'),
]

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # ... other URL patterns
    path('doctdrive_app/api/appointments/<int:pk>/update/', views.update_appointment, name='update_appointment'),
]




