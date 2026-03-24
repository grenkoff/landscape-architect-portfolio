from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import AboutSection, HeroSection, ServiceItem, SiteSettings


@admin.register(SiteSettings)
class SiteSettingsAdmin(TranslationAdmin):
    fieldsets = (
        (None, {"fields": ("site_title",)}),
        ("Контакты", {"fields": ("phone", "email")}),
        ("Соцсети", {"fields": ("telegram_url", "instagram_url", "vk_url", "whatsapp_url")}),
        ("SEO / Верификация", {"fields": ("yandex_verification", "google_verification")}),
    )

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(HeroSection)
class HeroSectionAdmin(TranslationAdmin):
    list_display = ("title", "is_active", "order")
    list_editable = ("is_active", "order")


@admin.register(ServiceItem)
class ServiceItemAdmin(TranslationAdmin):
    list_display = ("title", "order")
    list_editable = ("order",)


@admin.register(AboutSection)
class AboutSectionAdmin(TranslationAdmin):
    def has_add_permission(self, request):
        return not AboutSection.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
