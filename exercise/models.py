# coding=utf-8
# Python imports
# Django imports
from django.db import models
# Third party app imports
# Local app imports


class BodyPart(models.Model):
	name = models.CharField(null=False, blank=False, max_length=100, default='none')
	image = models.ImageField(upload_to='workout/bodyparts/', null=False, blank=False)
	
	def __unicode__(self):
		return self.name
	
	def __str__(self):
		return self.name


class Exercise(models.Model):
	name = models.CharField(null=False, blank=False, max_length=100, default='none')
	description = models.TextField(null=False, blank=False, max_length=300, default='none')
	image = models.ImageField(upload_to='workout/exercises/', null=False, blank=False)
	main_muscles = models.ManyToManyField('exercise.BodyPart', related_name='main_muscles')
	other_muscles = models.ManyToManyField('exercise.BodyPart', related_name='other_muscles', blank=True)
	
	def __unicode__(self):
		return self.name
	
	def __str__(self):
		return self.name


class Set(models.Model):
	reps = models.PositiveIntegerField()
	kgs = models.DecimalField(max_digits=5, decimal_places=2)
	rest = models.PositiveIntegerField()
	
	def __unicode__(self):
		return str(self.reps) + 'x' + str(self.kgs) + 'x' + str(self.rest) + "'"
	
	def __str__(self):
		return str(self.reps) + 'x' + str(self.kgs) + 'x' + str(self.rest) + "'"


class ExerciseSet(models.Model):
	exercise = models.ForeignKey('exercise.Exercise', null=True, on_delete=models.SET_NULL)
	set = models.ForeignKey('exercise.Set', null=True, on_delete=models.SET_NULL)
	
	def __unicode__(self):
		return self.exercise.name + " - " + str(self.set)
	
	def __str__(self):
		return self.exercise.name + " - " + str(self.set)
	

class TrainDay(models.Model):
	name = models.CharField(null=False, blank=False, max_length=100, default='none')
	exercise_sets = models.ManyToManyField('exercise.ExerciseSet')
	
	def __unicode__(self):
		return self.name
	
	def __str__(self):
		return self.name
	

class Routine(models.Model):
	TYPE_ROUTINE = (('BU', 'Bulking'), ('CU', 'Cutting'), ('MA', 'Maintaining'),)
	
	name = models.CharField(null=False, blank=False, max_length=100, default='none')
	description = models.TextField(null=False, blank=False, max_length=300, default='none')
	type = models.CharField(max_length=2, choices=TYPE_ROUTINE, default='MA')
	image = models.ImageField(upload_to='workout/routines/', null=False, blank=False)
	train_days = models.ManyToManyField('exercise.TrainDay')

	def __unicode__(self):
		return self.name
	
	def __str__(self):
		return self.name