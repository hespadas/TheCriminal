from django.contrib import admin

from .models.criminal import Criminal
from .models.classification import Classification

admin.site.register(Criminal)
admin.site.register(Classification)






