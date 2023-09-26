from django.contrib import admin
from .models import Post, Comment, Topic, UserProfile

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Topic)
admin.site.register(UserProfile)