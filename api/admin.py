from django.contrib import admin
from .models import Entry, Participant, Result, Survey_result
from import_export.admin import ImportExportModelAdmin


@admin.register(Entry, Participant, Result, Survey_result)
class ViewAdmin(ImportExportModelAdmin):
    pass
