from django.contrib import admin
from .models import Student





class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email', 'address', 'created_at', 'updated_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)
    ordering = ('-created_at',)


admin.site.register(Student, StudentAdmin)

admin.site.site_header = "Class Based CRUD Admin"
admin.site.site_title = "Class Based CRUD Admin Portal"
admin.site.index_title = "Welcome to Class Based CRUD Admin"

