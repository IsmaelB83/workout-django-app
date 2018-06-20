# coding=utf-8
# Python imports
# Django imports
from django.db import models
# Third party app imports
# Local app imports


class Program(models.Model):
	# Constants
	LEVEL = (('BE', 'Beginner'), ('IN', 'Intermediate'), ('AD', 'Advanced'),)
	TYPE = (('BU', 'Bulking'), ('CU', 'Cutting'), ('MA', 'Maintaining'),)

	# Attributes
	name = models.CharField(null = False, blank = False, max_length = 100)
	image = models.ImageField(upload_to = 'planner/program/', null = False, blank = True)
	summary = models.TextField(null = False, blank = True, max_length = 1500)
	level = models.CharField(max_length = 2, choices = LEVEL, default = 'IN')
	goal = models.CharField(max_length = 2, choices = TYPE, default = 'MA')
	start_date = models.DateTimeField()
	phases = models.ManyToManyField('planner.ProgramPhase')

	# Methods
	def __str__(self):
		return self.number + ' ' + self.workout.name


class ProgramPhase(models.Model):
	# Attributes
	order = models.PositiveIntegerField(blank = False, null = False)
	weeks_duration = models.PositiveIntegerField(blank = False, null = False)
	workout = models.ForeignKey('planner.Workout', null = True, on_delete = models.SET_NULL)

	# Methods
	def __str__(self):
		return self.order + ' - ' + self.workout.name


class Workout(models.Model):
	# Attributes
	name = models.CharField(null = False, blank = False, max_length = 100)
	image = models.ImageField(upload_to = 'planner/workout/', null = False, blank = False)
	day = models.ManyToManyField('planner.WorkoutDay')

	# Methods
	def __str__(self):
		return self.name


class WorkoutDay(models.Model):
	# Constants
	DAY = (
	('MO', 'Monday'), ('TU', 'Tuesday'), ('WE', 'Wednesday'), ('TH', 'Thursday'), ('FR', 'Friday'), ('SA', 'Saturday'),
	('SU', 'Sunday'),)

	# Attributes
	name = models.CharField(null = False, blank = False, max_length = 100)
	summary = models.TextField(null = False, blank = True, max_length = 1000)
	recommendations = models.TextField(null = False, blank = True, max_length = 1000)
	motivation_quotes = models.TextField(null = False, blank = True, max_length = 1000)
	day_of_week = models.CharField(max_length = 2, choices = DAY, default = 'MO')
	exercises = models.ManyToManyField('gym.ExerciseSet')

	# Methods
	def __str__(self):
		return self.name

