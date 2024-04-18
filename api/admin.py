from django.contrib import admin
from .models import Doctor, Patient, Specialization, Service, Visit


class VisitAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'patient', 'service', 'status']


admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Specialization)
admin.site.register(Service)
admin.site.register(Visit, VisitAdmin)
