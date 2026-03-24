from django.db import models


class SeoMixin(models.Model):
    meta_title = models.CharField(max_length=70, blank=True)
    meta_description = models.CharField(max_length=160, blank=True)

    class Meta:
        abstract = True


class SiteSettings(models.Model):
    site_title = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="logo/", blank=True, help_text="Site logo (SVG or PNG)")
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    telegram_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    vk_url = models.URLField(blank=True)
    whatsapp_url = models.URLField(blank=True)
    yandex_verification = models.CharField(
        max_length=100, blank=True, help_text="Яндекс.Вебмастер verification meta tag"
    )
    google_verification = models.CharField(
        max_length=100, blank=True, help_text="Google Search Console verification meta tag"
    )

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return self.site_title or "Site Settings"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1, defaults={"site_title": "Landscape Architect"})
        return obj


class HeroSection(SeoMixin):
    title = models.CharField(max_length=300)
    subtitle = models.TextField(blank=True)
    background_image = models.ImageField(upload_to="hero/")
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Hero Section"
        verbose_name_plural = "Hero Sections"

    def __str__(self):
        return self.title


class ServiceItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=50, blank=True, help_text="CSS icon class or emoji")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.title


class AboutSection(models.Model):
    heading = models.CharField(max_length=300)
    text = models.TextField()
    photo = models.ImageField(upload_to="about/", blank=True)

    class Meta:
        verbose_name = "About Section"
        verbose_name_plural = "About Section"

    def __str__(self):
        return self.heading or "About"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)
