# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone


class Post(models.Model):
    num=models.AutoField(primary_key=True)
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=20)
    
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title






class cafeinfo(models.Model):
	num=models.AutoField(primary_key=True)
	cafename=models.CharField(max_length=100)
	phone=models.CharField(max_length=20)
	x=models.CharField(max_length=30)
	y=models.CharField(max_length=30)
	roadAddr=models.CharField(max_length=50)

	def __str__(self):
		return self.cafename.encode('utf-8')

