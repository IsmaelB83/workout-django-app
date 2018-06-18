# coding=utf-8
# Python imports
# Django imports
from django.db import models
# Third party app imports
# Local app imports

# Buenas páginas de referencia
# https://www.freetrainers.com/
# http://musclecharts.net/


class MuscleGroup(models.Model):
	# Attributes
	name = models.CharField(null=False, blank=False, max_length=100)
	description = models.TextField(null=False, blank=True, max_length=1000)
	benefits = models.TextField(null=False, blank=True, max_length=1000)
	basics = models.TextField(null=False, blank=True, max_length=1000)
	image = models.ImageField(upload_to='workout/muscles/', null=False, blank=False)

	# Methods
	def __unicode__(self):
		return self.name
	
	def __str__(self):
		return self.name
	
	
class Muscle(models.Model):
	# Attributes
	name = models.CharField(null=False, blank=False, max_length=100)
	description = models.TextField(null=False, blank=True, max_length=1000)
	basics = models.TextField(null=False, blank=True, max_length=1000)
	image = models.ImageField(upload_to='workout/muscles/', null=False, blank=False)
	muscle_group = models.ForeignKey('exercise.MuscleGroup', null=True, on_delete=models.SET_NULL)

	# Methods
	def __unicode__(self):
		return self.name
	
	def __str__(self):
		return self.name


class Exercise(models.Model):
	# Attributes
	name = models.CharField(null=False, blank=False, max_length=100)
	description = models.TextField(null=False, blank=True, max_length=1000)
	instructions = models.TextField(null=False, blank=True, max_length=1000)
	tips = models.TextField(null=False, blank=True, max_length=1000)
	image = models.ImageField(upload_to='workout/exercises/', null=False, blank=False)
	primary_muscles = models.ManyToManyField('exercise.Muscle', related_name='primary_muscles')
	secondary_muscles = models.ManyToManyField('exercise.Muscle', related_name='secondary_muscles', blank=True)
	
	# Methods
	def __unicode__(self):
		return str(self.primary_muscles.all().first()) + " - " + self.name
	
	def __str__(self):
		return str(self.primary_muscles.all().first()) + " - " + self.name


class TrainingDay(models.Model):
	# Constants
	DAY = (('MO', 'Monday'), ('TU', 'Tuesday'), ('WE', 'Wednesday'), ('TH', 'Thursday'), ('FR', 'Friday'), ('SA', 'Saturday'), ('SU', 'Sunday'),)
	
	# Attributes
	name = models.CharField(null=False, blank=False, max_length=100)
	summary = models.TextField(null=False, blank=True, max_length=1000)
	recommendations = models.TextField(null=False, blank=True, max_length=1000)
	motivation_quotes = models.TextField(null=False, blank=True, max_length=1000)
	day_of_week = models.CharField(max_length=2, choices=DAY, default='MO')
	exercises = models.ManyToManyField('exercise.ExerciseSet')
	
	# Methods
	def __unicode__(self):
		return self.name
	
	def __str__(self):
		return self.name
	

class Workout(models.Model):
	# Constants
	LEVEL = (('BE', 'Beginner'), ('IN', 'Intermediate'), ('AD', 'Advanced'),)
	TYPE = (('BU', 'Bulking'), ('CU', 'Cutting'), ('MA', 'Maintaining'),)
	
	# Attributes
	name = models.CharField(null=False, blank=False, max_length=100)
	summary = models.TextField(null=False, blank=True, max_length=300)
	level = models.CharField(max_length=2, choices=LEVEL, default='IN')
	goal = models.CharField(max_length=2, choices=TYPE, default='MA')
	image = models.ImageField(upload_to='workout/routines/', null=False, blank=False)
	training_days = models.ManyToManyField('exercise.TrainingDay')
	
	# Methods
	def __unicode__(self):
		return self.name
	
	def __str__(self):
		return self.name
	
	
class ExerciseSet(models.Model):
	# Attributes
	exercise = models.ForeignKey('exercise.Exercise', null=True, on_delete=models.SET_NULL)
	reps = models.PositiveIntegerField()
	weight = models.DecimalField(max_digits=5, decimal_places=2)
	rest = models.PositiveIntegerField()
	
	# Methods
	def __unicode__(self):
		return self.exercise.name + " - " + str(self.reps) + 'x' + str(self.weight) + 'x' + str(self.rest) + "'"
	
	def __str__(self):
		return self.exercise.name + " - " + str(self.reps) + 'x' + str(self.weight) + 'x' + str(self.rest) + "'"
