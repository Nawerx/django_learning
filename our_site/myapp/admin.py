from django.contrib import admin

from myapp.models import Note

# Register your models here.

class Note_admin(admin.ModelAdmin):
    search_fields = ("title", "content")
    list_display = ("id", "title", "content", "created_at")



admin.site.register(Note, Note_admin)