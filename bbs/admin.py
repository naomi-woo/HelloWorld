from django.contrib import admin
from .models import User, Category, Post, Comment

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name', )}

admin.site.register(User)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post)
admin.site.register(Comment)
