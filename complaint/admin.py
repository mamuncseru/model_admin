from django.contrib import admin
from . models import ComplaintCategory
from . models import Complaint

admin.site.register(ComplaintCategory)
admin.site.register(Complaint)