from django.contrib import admin
from .models import Customer


# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['title', 'name', 'last_name', 'gender', 'created_by', 'created', 'status']
    readonly_fields = ['created']

    def last_name(self, obj):
        return obj.name + " " + obj.last_name


admin.site.register(Customer, CustomerAdmin)
