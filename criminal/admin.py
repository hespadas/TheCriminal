from django.contrib import admin

from .models.criminal import Criminal
from .models.crime import Crime
from .models.inventory import Inventory
from .models.classification import Classification

admin.site.register(Criminal)
admin.site.register(Classification)






