from django.db import models
from django.contrib.auth.models import User


class HospitalType(models.Model):
    type_name = models.CharField(null=False, unique=True, max_length=100)

    def __str__(self):
        return '{}'.format(self.type_name)

    def __repr__(self):
        return 'HospitalType(type_name={})'.format(self.type_name)


class Hospital(models.Model):
    name = models.CharField(null=False, blank=False, max_length=150)
    type = models.ForeignKey(HospitalType, null=False, on_delete=models.PROTECT, default=1)
    last_updated = models.DateTimeField(auto_now=True)
    total_normal_beds = models.IntegerField(null=False, default=0, blank=False)
    normal_beds_available = models.IntegerField(null=False, default=0, blank=False)
    total_beds_with_ventilator = models.IntegerField(null=False, default=0, blank=False)
    ventilator_beds_available = models.IntegerField(null=False, default=0, blank=False)
    total_icu_beds = models.IntegerField(null=False, default=0, blank=False)
    icu_beds_available = models.IntegerField(null=False, default=0, blank=False)
    fire_safety_compliance = models.BooleanField(null=False, default=False, blank=False)
    admin = models.ForeignKey(User, blank=True, null=True, on_delete=models.PROTECT)
    hospital_contact_number = models.CharField(null=False, blank=False, max_length=50, unique=True)
    contact_person_name = models.CharField(null=False, blank=False, max_length=50, unique=True)
    contact_person_mobile = models.CharField(null=False, blank=False, max_length=50, unique=True)
    liason_officer_phone = models.CharField(null=False, blank=False, max_length=50, unique=True)
    address = models.CharField(null=False, blank=False, max_length=200, unique=True)

    def __str__(self):
        return '{}'.format(self.name)