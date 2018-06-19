# coding=utf-8
# Python imports
# Django imports
from django.contrib import admin
# Third party app imports
# Local app imports
from .models import MuscleGroup, Muscle


# Register your models here.
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


admin.site.register(MuscleGroup, MuscleGroupModelAdmin)
admin.site.register(Muscle, MuscleModelAdmin)