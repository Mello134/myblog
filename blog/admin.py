from django.contrib import admin

# Register your models here.
from .models import Post #Импортировалм наш Post class. Нашу модель Post
admin.site.register(Post)