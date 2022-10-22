from django.db import models

# Create your models here.
class Eventhome(models.Model):
	event_image = models.ImageField(upload_to='event_images/')#поле ввода для загрузки изображений, upload_to="путь" - место где будет хранится
	event_text = models.CharField(max_length=300)#поле для ввода строк, максимальное количество символов 300
