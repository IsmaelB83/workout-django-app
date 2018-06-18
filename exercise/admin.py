# coding=utf-8
# Python imports
# Django imports
from django.contrib import admin
# Third party app imports
# Local app imports
from .models import MuscleGroup, Muscle, Exercise, ExerciseSet, TrainingDay, Workout


class MuscleGroupModelAdmin(admin.ModelAdmin):
	list_display = ["id", "name", "description", "benefits", "basics", "image"]
	list_display_links = ["id"]
	list_editable = ["name", "description", "benefits", "basics", "image"]
	list_filter = ["name"]
	search_fields = ["name"]
	
	class Meta:
		model = MuscleGroup
		

class MuscleModelAdmin(admin.ModelAdmin):
	list_display = ["id", "name", "description", "basics", "image", "muscle_group"]
	list_display_links = ["id"]
	list_editable = ["name", "description", "basics", "image", "muscle_group"]
	list_filter = ["name"]
	search_fields = ["name"]
	
	class Meta:
		model = Muscle


class ExerciseModelAdmin(admin.ModelAdmin):
	list_display = ["id", "name", "description", "instructions", "tips", "image"]
	list_display_links = ["id"]
	list_editable = ["name", "description", "instructions", "tips", "image"]
	list_filter = ["name"]
	search_fields = ["name"]
	
	class Meta:
		model = Exercise


class TrainingDayModelAdmin(admin.ModelAdmin):
	list_display = ["id", "name", "summary", "recommendations", "motivation_quotes", "day_of_week"]
	list_display_links = ["id"]
	list_editable = ["name", "summary", "recommendations", "motivation_quotes", "day_of_week"]
	list_filter = ["name"]
	search_fields = ["name"]

	class Meta:
		model = TrainingDay
		

class ExerciseSetModelAdmin(admin.ModelAdmin):
	list_display = ["id", "exercise", "reps", "weight", "rest"]
	list_display_links = ["id"]
	list_editable = ["exercise", "reps", "weight", "rest"]
	list_filter = ["exercise"]
	search_fields = ["exercise"]

	class Meta:
		model = ExerciseSet

		
class WorkoutModelAdmin(admin.ModelAdmin):
	list_display = ["id", "name", "summary", "level", "goal", "image"]
	list_display_links = ["id"]
	list_editable = ["name", "summary", "level", "goal", "image"]
	list_filter = ["name", "summary", "level", "goal", "image"]
	search_fields = ["name", "summary", "level", "goal", "image"]
	
	class Meta:
		model = Workout
		
		
admin.site.register(MuscleGroup, MuscleGroupModelAdmin)
admin.site.register(Muscle, MuscleModelAdmin)
admin.site.register(Exercise, ExerciseModelAdmin)
admin.site.register(ExerciseSet, ExerciseSetModelAdmin)
admin.site.register(TrainingDay, TrainingDayModelAdmin)
admin.site.register(Workout, WorkoutModelAdmin)
