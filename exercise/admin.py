# coding=utf-8
# Python imports
# Django imports
from django.contrib import admin
# Third party app imports
# Local app imports
from .models import MuscleGroup, Muscle, Exercise, ExerciseSet, WorkoutPhase, WorkoutTrainingDay, Workout


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


class ExerciseSetModelAdmin(admin.ModelAdmin):
	list_display = ["id", "exercise", "time", "reps", "weight", "rest"]
	list_display_links = ["id"]
	list_editable = ["exercise", "time", "reps", "weight", "rest"]
	list_filter = ["exercise"]
	search_fields = ["exercise"]

	class Meta:
		model = ExerciseSet


class WorkoutPhaseModelAdmin(admin.ModelAdmin):
	list_display = ["id", "number", "weeks_duration"]
	list_display_links = ["id"]
	list_editable = ["number", "weeks_duration"]
	list_filter = ["number"]
	search_fields = ["number"]

	class Meta:
		model = WorkoutPhase


class WorkoutTrainingDayModelAdmin(admin.ModelAdmin):
	list_display = ["id", "name", "summary", "recommendations", "motivation_quotes", "day_of_week"]
	list_display_links = ["id"]
	list_editable = ["name", "summary", "recommendations", "motivation_quotes", "day_of_week"]
	list_filter = ["name"]
	search_fields = ["name"]

	class Meta:
		model = WorkoutTrainingDay


class WorkoutModelAdmin(admin.ModelAdmin):
	list_display = ["id", "name", "summary", "level", "goal", "image"]
	list_display_links = ["id"]
	list_editable = ["name", "summary", "level", "goal", "image"]
	list_filter = ["name"]
	search_fields = ["name"]

	class Meta:
		model = Workout


admin.site.register(MuscleGroup, MuscleGroupModelAdmin)
admin.site.register(Muscle, MuscleModelAdmin)
admin.site.register(Exercise, ExerciseModelAdmin)
admin.site.register(ExerciseSet, ExerciseSetModelAdmin)
admin.site.register(WorkoutPhase, WorkoutPhaseModelAdmin)
admin.site.register(WorkoutTrainingDay, WorkoutTrainingDayModelAdmin)
admin.site.register(Workout, WorkoutModelAdmin)
