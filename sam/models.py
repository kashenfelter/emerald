from __future__ import unicode_literals

from django.db import models

class IntegerBlankStringField(models.IntegerField):
    def get_prep_value(self, value):
        if value == '':
            return 0
        return value

class SamRecord(models.Model):

    duns = IntegerBlankStringField(null=True)
    cage_code = models.CharField(max_length=5, null=True)
    registration_date = models.DateTimeField(null=True)
    expiration_date = models.DateTimeField(null=True)
    last_update_date = models.DateTimeField(null=True)
    activation_date = models.DateTimeField(null=True)
    legal_name = models.CharField(max_length=120, null=True)
    name = models.CharField(max_length=120, null=True)
    address_1 = models.CharField(max_length=150, null=True)
    address_2 = models.CharField(max_length=150, null=True)
    city = models.CharField(max_length=40, null=True)
    state = models.CharField(max_length=55, null=True)
    zip_code = models.CharField(max_length=50, null=True)
    country_code = models.CharField(max_length=3, null=True)
    business_start_date = models.DateTimeField(null=True)
    fiscal_year_end_close_date = models.DateTimeField(null=True)
    url = models.URLField(null=True)
    entity_structure = models.CharField(max_length=2, null=True)
    state_of_incorporation = models.CharField(max_length=2, null=True)
    business_type_counter = IntegerBlankStringField(null=True)
    buysiness_type_string = models.CharField(max_length=220, null=True)
    primary_naics = models.CharField(max_length=6, null=True)
    email_address = models.EmailField(max_length=80, null=True)
    phone = models.CharField(max_length=30, null=True)
    phone_ext = models.CharField(max_length=25, null=True)
    naics_exception_counter = models.CharField(max_length=4, null=True)
    naics_exception_string = models.CharField(max_length=1100, null=True)
    naics = models.CharField(max_length=2000, null=True)
    sba_business_types_counter = models.CharField(max_length=4, null=True)
    sba_business_types_string = models.CharField(max_length=125, null=True)
    no_public_display_flag = models.CharField(max_length=4, null=True)

    def __unicode__(self):
        return u'{0}'.format(self.legal_name)

