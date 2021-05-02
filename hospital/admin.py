from django.contrib import admin

# Register your models here.
from hospital.models import Hospital, HospitalType


class HospitalAdmin(admin.ModelAdmin):
    raw_id_fields = ("admin",)


admin.site.register(Hospital, HospitalAdmin)
admin.site.register(HospitalType)