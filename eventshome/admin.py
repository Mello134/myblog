from django.contrib import admin

# Register your models here.
from .models import Eventhome #Импортировалм наш Eventhome class. Нашу модель Eventhome
admin.site.register(Eventhome)