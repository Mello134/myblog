from django.db import models

# Create your models here.
class Post(models.Model):
	title =  models.CharField(max_length=300)#поле для ввода строк, максимальное количество символов 300
	date = models.DateTimeField()#поле дата время
	text = models.TextField()#для большого тестового поля
	image = models.ImageField(upload_to='event_images/')#поле ввода для загрузки изображений, upload_to="путь" - место где будет хранится

	def get_summary(self):#создаём функцию - для получения краткой сводуки
		return self.text[:70]#вернёт только 70 символов из текста