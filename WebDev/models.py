from tkinter.constants import CASCADE
from django.db import models
from django.contrib.auth.models import User

  # Developers Table
class Developers(models.Model):
  DeveloperID = models.BigAutoField(auto_created=True, primary_key=True, blank=False, unique=True)
  FirstName = models.CharField(max_length=255, blank=False)
  LastName = models.CharField(max_length=255, blank=False)
  Gender = models.CharField(max_length=255, null=True)
  Email = models.CharField(max_length=255, blank=False )
  MobileNumber = models.CharField(max_length=255, blank=False)
  HomeNumber = models.CharField(max_length=255, null=True)
  def __str__(self):
    return '%s %s %s' % (self.FirstName, self.LastName, self.DeveloperID)
  


CHOICES = (
    ('Pending','Pending'),
    ('Paid', 'Paid'),
)

# Billing Table
class Billing(models.Model):
  BillingID = models.BigAutoField(auto_created=True, primary_key=True, blank=False, unique=True)
  ClientID = models.ForeignKey(User, on_delete=models.CASCADE)
  AmountOwed = models.DecimalField(max_digits=100, decimal_places=2, blank=False)
  PaymentStatus = models.CharField(max_length=255,choices=CHOICES, blank=False)
  def __str__(self):
    return '%s ' % (self.ClientID)



# admin Website details Table
class Website_details(models.Model):
  WebsiteID = models.BigAutoField(auto_created=True, primary_key=True, blank=False, unique=True)
  ClientID = models.ForeignKey(User, on_delete=models.CASCADE)
  DeveloperID = models.ForeignKey(Developers, blank=True, null=True, on_delete=models.CASCADE)
  WebsiteName = models.CharField(max_length=255, blank=False)
  WebsiteType = models.CharField(max_length=255, blank=False)
  WebsiteStatus = models.CharField(max_length=255, blank=True)
  DueDate = models.CharField(max_length=255, blank=True, null=True)
  def __str__(self):
    return '%s %s ' % (self.WebsiteName, self.WebsiteID)

