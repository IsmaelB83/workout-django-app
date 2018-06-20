# coding=utf-8
# Python imports
# Django imports
from django.contrib import admin
# Third party app imports
# Local app imports
from .models import Exercise, ExerciseSet, Set


class ExerciseModelAdmin(admin.ModelAdmin):
	list_display = ["id", "name", "description", "instructions", "tips", "image"]
	list_display_links = ["id"]
	list_editable = ["name", "description", "instructions", "tips", "image"]
	list_filter = ["name"]
	search_fields = ["name"]

	class Meta:
		model = Exercise


class ExerciseSetModelAdmin(admin.ModelAdmin):
	list_display = ["id", "exercise", "number_of_sets"]
	list_display_links = ["id"]
	list_editable = ["exercise", "number_of_sets"]
	list_filter = ["exercise"]
	search_fields = ["exercise"]

	class Meta:
		model = ExerciseSet


class SetModelAdmin(admin.ModelAdmin):
	list_display = ["id", "reps", "reps_unit", "weight", "weight_unit"]
	list_display_links = ["id"]
	list_editable = ["reps", "reps_unit", "weight", "weight_unit"]
	list_filter = ["reps", "reps_unit", "weight", "weight_unit"]
	search_fields = ["reps", "reps_unit", "weight", "weight_unit"]

	class Meta:
		model = Set


admin.site.register(Exercise, ExerciseModelAdmin)
admin.site.register(ExerciseSet, ExerciseSetModelAdmin)
admin.site.register(Set, SetModelAdmin)

