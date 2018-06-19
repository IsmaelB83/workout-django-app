# coding=utf-8
# Python imports
# Django imports
from django.db import models
# Third party app imports
# Local app imports


class MuscleGroup(models.Model):
	# Attributes
	name = models.CharField(null = False, blank = False, max_length = 100)
	description = models.TextField(null = False, blank = True, max_length = 1000)
	benefits = models.TextField(null = False, blank = True, max_length = 1000)
	basics = models.TextField(null = False, blank = True, max_length = 1000)
	image = models.ImageField(upload_to = 'body/muscle_groups/', null = False, blank = False)

	# Methods
	def __str__(self):
		return self.name


class Muscle(models.Model):
	# Attributes
	name = models.CharField(null = False, blank = False, max_length = 100)
	description = models.TextField(null = False, blank = True, max_length = 1000)
	basics = models.TextField(null = False, blank = True, max_length = 1000)
	image = models.ImageField(upload_to = 'body/muscles/', null = False, blank = False)
	muscle_group = models.ForeignKey('body.MuscleGroup', null = True, on_delete = models.SET_NULL)

	# Methods
	def __str__(self):
		return self.name
