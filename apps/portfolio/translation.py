from modeltranslation.translator import TranslationOptions, translator

from .models import Category, Project, ProjectImage


class CategoryTranslation(TranslationOptions):
    fields = ("name",)


class ProjectTranslation(TranslationOptions):
    fields = ("title", "description", "location", "meta_title", "meta_description")


class ProjectImageTranslation(TranslationOptions):
    fields = ("caption",)


translator.register(Category, CategoryTranslation)
translator.register(Project, ProjectTranslation)
translator.register(ProjectImage, ProjectImageTranslation)
