from modeltranslation.translator import TranslationOptions, translator

from .models import AboutSection, HeroSection, ServiceItem, SiteSettings


class SiteSettingsTranslation(TranslationOptions):
    fields = ("site_title",)


class HeroSectionTranslation(TranslationOptions):
    fields = ("title", "subtitle", "meta_title", "meta_description")


class ServiceItemTranslation(TranslationOptions):
    fields = ("title", "description")


class AboutSectionTranslation(TranslationOptions):
    fields = ("heading", "text")


translator.register(SiteSettings, SiteSettingsTranslation)
translator.register(HeroSection, HeroSectionTranslation)
translator.register(ServiceItem, ServiceItemTranslation)
translator.register(AboutSection, AboutSectionTranslation)
