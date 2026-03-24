from django.test import TestCase, override_settings

from .models import AboutSection, HeroSection, ServiceItem, SiteSettings


class SiteSettingsModelTest(TestCase):
    def test_singleton_pattern(self):
        SiteSettings.objects.create(site_title="First")
        s2 = SiteSettings(site_title="Second")
        s2.save()
        self.assertEqual(SiteSettings.objects.count(), 1)
        self.assertEqual(SiteSettings.objects.first().site_title, "Second")

    def test_load_creates_default(self):
        self.assertEqual(SiteSettings.objects.count(), 0)
        settings = SiteSettings.load()
        self.assertEqual(SiteSettings.objects.count(), 1)
        self.assertEqual(settings.pk, 1)

    def test_str(self):
        s = SiteSettings(site_title="Test Site")
        self.assertEqual(str(s), "Test Site")


class AboutSectionModelTest(TestCase):
    def test_singleton_pattern(self):
        AboutSection.objects.create(heading="First", text="Text")
        a2 = AboutSection(heading="Second", text="Text 2")
        a2.save()
        self.assertEqual(AboutSection.objects.count(), 1)
        self.assertEqual(AboutSection.objects.first().heading, "Second")


class HeroSectionModelTest(TestCase):
    def test_ordering(self):
        HeroSection.objects.create(title="Second", order=2, background_image="hero/test.jpg")
        HeroSection.objects.create(title="First", order=1, background_image="hero/test.jpg")
        heroes = list(HeroSection.objects.values_list("title", flat=True))
        self.assertEqual(heroes, ["First", "Second"])

    def test_str(self):
        h = HeroSection(title="Test Hero")
        self.assertEqual(str(h), "Test Hero")


class ServiceItemModelTest(TestCase):
    def test_str(self):
        s = ServiceItem(title="Garden Design")
        self.assertEqual(str(s), "Garden Design")


@override_settings(ROOT_URLCONF="config.urls")
class HomeViewTest(TestCase):
    def test_home_page_returns_200(self):
        response = self.client.get("/ru/")
        self.assertEqual(response.status_code, 200)

    def test_home_page_en_returns_200(self):
        response = self.client.get("/en/")
        self.assertEqual(response.status_code, 200)

    def test_home_page_uses_correct_template(self):
        response = self.client.get("/ru/")
        self.assertTemplateUsed(response, "core/home.html")

    def test_home_page_context(self):
        response = self.client.get("/ru/")
        self.assertIn("heroes", response.context)
        self.assertIn("services", response.context)
        self.assertIn("featured_projects", response.context)

    def test_home_page_with_content(self):
        SiteSettings.objects.create(site_title="Test Portfolio")
        HeroSection.objects.create(title="Welcome", background_image="hero/test.jpg", is_active=True)
        ServiceItem.objects.create(title="Design", description="Landscape design")
        response = self.client.get("/ru/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome")
        self.assertContains(response, "Design")


@override_settings(ROOT_URLCONF="config.urls")
class RobotsTxtTest(TestCase):
    def test_robots_txt_returns_200(self):
        response = self.client.get("/robots.txt")
        self.assertEqual(response.status_code, 200)
        self.assertIn("text/plain", response["Content-Type"])

    def test_robots_txt_contains_sitemap(self):
        response = self.client.get("/robots.txt")
        self.assertContains(response, "Sitemap:")
        self.assertContains(response, "sitemap.xml")


@override_settings(ROOT_URLCONF="config.urls")
class SitemapTest(TestCase):
    def test_sitemap_returns_200(self):
        response = self.client.get("/sitemap.xml")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<urlset")


@override_settings(ROOT_URLCONF="config.urls")
class LanguageSwitchTest(TestCase):
    def test_set_language_endpoint(self):
        response = self.client.post("/i18n/setlang/", {"language": "en"}, follow=True)
        self.assertEqual(response.status_code, 200)


class SiteSettingsAdminTest(TestCase):
    def setUp(self):
        from django.contrib.auth.models import User

        self.admin = User.objects.create_superuser("admin", "admin@test.com", "password")
        self.client.login(username="admin", password="password")

    def test_site_settings_admin_accessible(self):
        response = self.client.get("/ru/admin/core/sitesettings/")
        self.assertEqual(response.status_code, 200)

    def test_site_settings_add_when_none_exists(self):
        response = self.client.get("/ru/admin/core/sitesettings/add/")
        self.assertEqual(response.status_code, 200)

    def test_site_settings_no_add_when_exists(self):
        SiteSettings.objects.create(site_title="Test")
        response = self.client.get("/ru/admin/core/sitesettings/add/")
        self.assertEqual(response.status_code, 403)
