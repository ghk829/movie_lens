from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Users(models.Model):
	user_id = models.IntegerField(primary_key=True)
	age = models.IntegerField()
	gender = models.CharField(max_length=100)
	occupation = models.CharField(max_length=100)
	zip_code = models.IntegerField()
	
class Items(models.Model):
	item_id = models.IntegerField(primary_key=True)
	item_title = models.CharField(max_length=100)
	url = models.CharField(max_length=200,null=True)


class Ratings(models.Model):
	RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
	user=models.ForeignKey(Users)
	item=models.ForeignKey(Items)
	rating =models.IntegerField(choices=RATING_CHOICES)
	timestamp = models.IntegerField()

class Recommend(models.Model):
	user=models.ForeignKey(Users)
	item=models.ForeignKey(Items)
	rating=models.IntegerField()