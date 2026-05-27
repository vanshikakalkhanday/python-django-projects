from django.contrib import admin

from .models import Student

class StudentAdmin(admin.ModelAdmin):

    list_display = ('name', 'age', 'email')

    search_fields = ('name',)

    list_filter = ('age',)

    ordering = ('name',)

admin.site.register(Student, StudentAdmin)
 