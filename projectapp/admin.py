from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Person, FileUpload
# Register your models here.
admin.site.register(FileUpload)
@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    list_display=('name','email','location')


    
