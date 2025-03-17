from django.contrib import admin
from . models import *

myModels = [Developers, Billing, Website_details]  # iterable list
admin.site.register(myModels)

#http://127.0.0.1:8000/admin/