# coding=utf-8
# Python imports
# Django imports
from django.contrib import admin
# Third party app imports
# Local app imports
from .models import Program, ProgramPhase, Workout, WorkoutDay


class ProgramModelAdmin(admin.ModelAdmin):
	list_display = ["id", "name", "image", "summary", "level", "goal", "start_date"]
	list_display_links = ["id"]
	list_editable = ["name", "image", "summary", "level", "goal", "start_date"]
	list_filter = ["name"]
	search_fields = ["name"]

	class Meta:
		model = Program


class ProgramPhaseModelAdmin(admin.ModelAdmin):
	list_display = ["id", "order", "weeks_duration", "workout"]
	list_display_links = ["id"]
	list_editable = ["order", "weeks_duration", "workout"]
	list_filter = ["order"]
	search_fields = ["order"]

	class Meta:
		model = ProgramPhase


class WorkoutModelAdmin(admin.ModelAdmin):
	list_display = ["id", "name", "image"]
	list_display_links = ["id"]
	list_editable = ["name", "image"]
	list_filter = ["name"]
	search_fields = ["name"]

	class Meta:
		model = Workout


class WorkoutDayModelAdmin(admin.ModelAdmin):
	list_display = ["id", "name", "summary", "recommendations", "motivation_quotes", "day_of_week"]
	list_display_links = ["id"]
	list_editable = ["name", "summary", "recommendations", "motivation_quotes", "day_of_week"]
	list_filter = ["name"]
	search_fields = ["name"]

	class Meta:
		model = WorkoutDay


admin.site.register(Program, ProgramModelAdmin)
admin.site.register(ProgramPhase, ProgramPhaseModelAdmin)
admin.site.register(Workout, WorkoutModelAdmin)
admin.site.register(WorkoutDay, WorkoutDayModelAdmin)
