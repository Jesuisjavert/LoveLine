from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Community)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(CategoryGroup)
admin.site.register(CourseTotal)
admin.site.register(CourseDetail)
admin.site.register(Review)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(CoursePost)