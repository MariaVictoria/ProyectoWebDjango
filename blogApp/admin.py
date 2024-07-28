from django.contrib import admin
from .models import Post, Categoria


class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Categoria, CategoriaAdmin)


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Post, PostAdmin)