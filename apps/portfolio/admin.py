from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline

from .models import Category, Project, ProjectImage


class ProjectImageInline(TranslationTabularInline):
    model = ProjectImage
    extra = 1


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ("name", "slug", "order")
    list_editable = ("order",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Project)
class ProjectAdmin(TranslationAdmin):
    list_display = ("title", "category", "year", "is_published", "order")
    list_filter = ("category", "is_published", "year")
    list_editable = ("is_published", "order")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ProjectImageInline]
    fieldsets = (
        (None, {"fields": ("title", "slug", "category", "description")}),
        ("Детали", {"fields": ("location", "year", "cover_image")}),
        ("Публикация", {"fields": ("is_published", "order")}),
        ("SEO", {"fields": ("meta_title", "meta_description"), "classes": ("collapse",)}),
    )
