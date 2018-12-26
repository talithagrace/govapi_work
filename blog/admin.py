from django.contrib import admin
from .models import Opencons, Legislation, Consultations, News

admin.site.register(Opencons)
admin.site.register(Legislation)
admin.site.register(News)
admin.site.register(Consultations)

# Register your models here.
