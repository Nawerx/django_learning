from django.contrib import admin

from myapp.models import Note, User

# Register your models here.


class Note_admin(admin.ModelAdmin):
    search_fields = ("title", "content")
    list_display = ("id", "title", "content", "created_at", "updated_at")
    list_display_links = ("title",)


class User_admin(admin.ModelAdmin):
    search_fields = ("name", "email")
    list_display = ("id", "name", "email")
    list_display_links = ("name",)


admin.site.register(Note, Note_admin)
admin.site.register(User, User_admin)
