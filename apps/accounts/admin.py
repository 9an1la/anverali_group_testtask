from django.contrib import admin
from .models import CustomUser, CustomerProfile, ExecutorProfile


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'is_staff', 'is_active', 'first_name',
                    'last_name', 'email', 'date_joined', 'is_customer',
                    'is_executor']


@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ['customer', 'contact_info', 'experience']
    raw_id_fields = ['customer']


@admin.register(ExecutorProfile)
class ExecutorProfileAdmin(admin.ModelAdmin):
    list_display = ['executor', 'contact_info', 'experience']
    raw_id_fields = ['executor']
