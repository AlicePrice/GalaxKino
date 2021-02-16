from django.db import models
from uuid import uuid4
from django.contrib.auth import get_user_model
#from django.core.files.storage import FileSystemStorage

ages_qualif = (
	('0', '6+'),
	('1', '12+'),
	('2', '16+'),
	('3', '18+'),
)
cat_films = (
	('0', 'Скоро в кино'),
	('1', 'В прокате'),
	('2', 'Показ окончен'),
)

class Film(models.Model):
	uuid = models.CharField(max_length=36, default=str(uuid4()))
	category = models.CharField(max_length=1, default='0', choices=cat_films)

	name = models.CharField(max_length=200)
	producer = models.CharField(max_length=100)
	at_box = models.DateField()
	duration = models.IntegerField(default=0)
	age_qualif = models.CharField(max_length=1, default='2', choices=ages_qualif)
	genre = models.TextField()
	country = models.CharField(max_length=100)

	actors = models.TextField(default='', blank=True, null=True)

	poster = models.ImageField(upload_to='media/posters/')
	description = models.TextField()
	rate = models.FloatField(default=0.0)

	trailer_one = models.URLField()
	trailer_two = models.URLField(default='', blank=True, null=True)
	trailer_thr = models.URLField(default='', blank=True, null=True)

	def __str__(self):
		return self.name

class Profile(models.Model):
	uuid = models.CharField(max_length=36, default=str(uuid4()))

	user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)

	age = models.IntegerField(default=0)
	sex = models.BooleanField(default=False)

	phone_number = models.CharField(max_length=10)
	email = models.EmailField()
	date_reg = models.DateTimeField(auto_now_add=True)

	is_active = models.BooleanField(default=True)
	is_blocked = models.BooleanField(default=False)

	def __str__(self):
		return f"{self.first_name} {self.last_name}"

class Session(models.Model):
	uuid = models.CharField(max_length=36, default=str(uuid4()))

	film = models.ForeignKey(Film, on_delete=models.CASCADE)
	time = models.TimeField()

	def __str__(self):
		return f"{self.film} {self.time}"

class Comment(models.Model):
	uuid = models.CharField(max_length=36, default=str(uuid4()))

	film = models.ForeignKey(Film, on_delete=models.CASCADE)
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
	datetime = models.DateTimeField(auto_now_add=True)
	text = models.TextField()

	rate = models.IntegerField(default=0)

	def __str__(self):
		return self.text

