from django.contrib import admin
from .models import CustomUser,Appointment,Doctor

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Appointment)
admin.site.register(Doctor)




