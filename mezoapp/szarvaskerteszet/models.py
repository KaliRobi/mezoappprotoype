import datetime
from django.db import models
# Create your models here.


class OwnerDetails(models.Model):

    inser_time = models.DateField(default=datetime.date.today)
    update_time = models.DateField(default=datetime.date.today)
    user_name = models.CharField(max_length=200)
    contact_phone = models.CharField(max_length=15)
    contact_email = models.CharField(max_length=40)
    short_intorduction = models.CharField(max_length=500)

    def __str__(self):
        return str(self.id)

class BusinessTypes(models.Model):

    type_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.type_name

class BusinessDetails(models.Model):

    owner = models.ForeignKey(OwnerDetails, on_delete=models.CASCADE)
    business_name  =  models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    type_of_business = models.ForeignKey(BusinessTypes, on_delete=models.CASCADE)
    description = models.TextField()
    established_date = models.DateField()

    def __str__(self):
        return self.business_name

