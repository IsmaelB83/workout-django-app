# coding=utf-8
# Python imports
# Django imports
from django.contrib import admin
# Third party app imports
# Local app imports
from .models import BodyPart, Exercise, Set, ExerciseSet, TrainDay, Routine


class BodyPartModelAdmin(admin.ModelAdmin):
	list_display = ["id", "name", "image"]
	list_display_links = ["id"]
	list_editable = ["name", "image"]
	list_filter = ["name"]
	search_fields = ["name"]
	
	class Meta:
		model = BodyPart


class ExerciseModelAdmin(admin.ModelAdmin):
	list_display = ["id", "name", "description", "image"]
	list_display_links = ["id"]
	list_editable = ["name", "description"]
	list_filter = ["name", "description"]
	search_fields = ["name", "description"]
	
	class Meta:
		model = Exercise


class SetModelAdmin(admin.ModelAdmin):
	list_display = ["id", "reps", "kgs", "rest"]
	list_display_links = ["id"]
	list_editable = ["reps", "kgs", "rest"]
	list_filter = ["reps", "kgs", "rest"]
	search_fields = ["reps", "kgs", "rest"]

	class Meta:
		model = Set


class ExerciseSetModelAdmin(admin.ModelAdmin):
	list_display = ["id", "exercise", "set"]
	list_display_links = ["id"]
	list_editable = ["exercise", "set"]
	list_filter = ["exercise", "set"]
	search_fields = ["exercise", "set"]

	class Meta:
		model = ExerciseSet


class TrainDayModelAdmin(admin.ModelAdmin):
	list_display = ["id", "name"]
	list_display_links = ["id"]
	list_editable = ["name"]
	list_filter = ["name"]
	search_fields = ["name"]

	class Meta:
		model = TrainDay
		
		
class RoutineModelAdmin(admin.ModelAdmin):
	list_display = ["id", "name", "description", "type", "image"]
	list_display_links = ["id"]
	list_editable = ["name", "description", "type", "image"]
	list_filter = ["name", "description", "type", "image"]
	search_fields = ["name", "description", "type", "image"]

	class Meta:
		model = Routine
		
		
admin.site.register(BodyPart, BodyPartModelAdmin)
admin.site.register(Exercise, ExerciseModelAdmin)
admin.site.register(Set, SetModelAdmin)
admin.site.register(ExerciseSet, ExerciseSetModelAdmin)
admin.site.register(TrainDay, TrainDayModelAdmin)
admin.site.register(Routine, RoutineModelAdmin)
