# articles/admin.py
from django.contrib import admin
from .models import Article, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]
    list_display = [
        "id",
        "title",
        "body",
        "author",
        "date",
    ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)