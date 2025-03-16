from django import forms
from .models import Developers, Website_details, Billing

class dev_form(forms.ModelForm):
    class Meta:
        model=Developers
        fields=['DeveloperID', 'FirstName', 'LastName', 'Gender', 'Email', 'MobileNumber', 'HomeNumber']

class details_form(forms.ModelForm):
    class Meta:
        model=Website_details
        fields=['WebsiteID', 'ClientID', 'DeveloperID', 'WebsiteName','WebsiteType','WebsiteStatus','DueDate']

class billing_form(forms.ModelForm):
    class Meta:
        model=Billing
        fields=['BillingID', 'ClientID', 'AmountOwed', 'PaymentStatus']





        




        