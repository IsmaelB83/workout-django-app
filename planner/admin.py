# coding=utf-8
# Python imports
# Django imports
from django.contrib import admin
# Third party app imports
# Local app imports
from .models import Program, ProgramPhase, Workout, WorkoutDay, WorkoutSession


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
	list_display = ["id", "day_of_week", "session"]
	list_display_links = ["id"]
	list_editable = ["day_of_week", "session"]
	list_filter = ["day_of_week"]
	search_fields = ["day_of_week"]

	class Meta:
		model = WorkoutDay


class WorkoutSessionModelAdmin(admin.ModelAdmin):
	list_display = ["id", "name", "summary", "recommendations", "motivation_quotes"]
	list_display_links = ["id"]
	list_editable = ["name", "summary", "recommendations", "motivation_quotes"]
	list_filter = ["name"]
	search_fields = ["name"]

	class Meta:
		model = WorkoutSession


admin.site.register(Program, ProgramModelAdmin)
admin.site.register(ProgramPhase, ProgramPhaseModelAdmin)
admin.site.register(Workout, WorkoutModelAdmin)
admin.site.register(WorkoutDay, WorkoutDayModelAdmin)
admin.site.register(WorkoutSession, WorkoutSessionModelAdmin)

