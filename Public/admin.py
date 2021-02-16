from django.contrib import admin
from .models import Film, Profile, Session, Comment

admin.site.register(Film)
admin.site.register(Session)
admin.site.register(Comment)
admin.site.register(Profile)
