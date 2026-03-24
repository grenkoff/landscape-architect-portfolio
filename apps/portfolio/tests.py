from django.test import TestCase, override_settings

from .models import Category, Project, ProjectImage


class CategoryModelTest(TestCase):
    def test_str(self):
        c = Category(name="Residential")
        self.assertEqual(str(c), "Residential")

    def test_ordering(self):
        Category.objects.create(name="B", slug="b", order=2)
        Category.objects.create(name="A", slug="a", order=1)
        names = list(Category.objects.values_list("name", flat=True))
        self.assertEqual(names, ["A", "B"])


class ProjectModelTest(TestCase):
    def test_str(self):
        p = Project(title="Park Design")
        self.assertEqual(str(p), "Park Design")

    def test_ordering(self):
        Project.objects.create(title="B", slug="b", description="desc", cover_image="test.jpg", order=2)
        Project.objects.create(title="A", slug="a", description="desc", cover_image="test.jpg", order=1)
        titles = list(Project.objects.values_list("title", flat=True))
        self.assertEqual(titles, ["A", "B"])

    def test_published_filter(self):
        Project.objects.create(title="Published", slug="pub", description="d", cover_image="t.jpg", is_published=True)
        Project.objects.create(title="Draft", slug="draft", description="d", cover_image="t.jpg", is_published=False)
        published = Project.objects.filter(is_published=True)
        self.assertEqual(published.count(), 1)
        self.assertEqual(published.first().title, "Published")


class ProjectImageModelTest(TestCase):
    def test_str_with_caption(self):
        p = Project.objects.create(title="Test", slug="test", description="d", cover_image="t.jpg")
        img = ProjectImage(project=p, image="test.jpg", caption="Front view")
        self.assertEqual(str(img), "Front view")

    def test_str_without_caption(self):
        p = Project.objects.create(title="Test", slug="test", description="d", cover_image="t.jpg")
        img = ProjectImage.objects.create(project=p, image="test.jpg")
        self.assertEqual(str(img), f"Image {img.pk}")


@override_settings(ROOT_URLCONF="config.urls")
class ProjectListViewTest(TestCase):
    def test_empty_list_returns_200(self):
        response = self.client.get("/ru/portfolio/")
        self.assertEqual(response.status_code, 200)

    def test_list_shows_published_projects(self):
        p1 = Project.objects.create(
            title="Visible", slug="visible", description="d", cover_image="t.jpg", is_published=True
        )
        p1.title_ru = "Visible"
        p1.save()
        p2 = Project.objects.create(
            title="Hidden", slug="hidden", description="d", cover_image="t.jpg", is_published=False
        )
        p2.title_ru = "Hidden"
        p2.save()
        response = self.client.get("/ru/portfolio/")
        self.assertContains(response, "Visible")
        self.assertNotContains(response, "Hidden")

    def test_category_filter(self):
        cat = Category.objects.create(name="Parks", slug="parks")
        Project.objects.create(
            title="Park Project", slug="park", description="d", cover_image="t.jpg", category=cat, is_published=True
        )
        Project.objects.create(title="Other", slug="other", description="d", cover_image="t.jpg", is_published=True)
        response = self.client.get("/ru/portfolio/?category=parks")
        self.assertContains(response, "Park Project")
        self.assertNotContains(response, "Other")

    def test_en_list_returns_200(self):
        response = self.client.get("/en/portfolio/")
        self.assertEqual(response.status_code, 200)


@override_settings(ROOT_URLCONF="config.urls")
class ProjectDetailViewTest(TestCase):
    def test_detail_returns_200(self):
        Project.objects.create(title="Test", slug="test-project", description="desc", cover_image="t.jpg")
        response = self.client.get("/ru/portfolio/test-project/")
        self.assertEqual(response.status_code, 200)

    def test_detail_uses_correct_template(self):
        Project.objects.create(title="Test", slug="test-project", description="desc", cover_image="t.jpg")
        response = self.client.get("/ru/portfolio/test-project/")
        self.assertTemplateUsed(response, "portfolio/project_detail.html")

    def test_unpublished_project_returns_404(self):
        Project.objects.create(title="Draft", slug="draft", description="desc", cover_image="t.jpg", is_published=False)
        response = self.client.get("/ru/portfolio/draft/")
        self.assertEqual(response.status_code, 404)

    def test_detail_contains_title(self):
        Project.objects.create(title="Beautiful Garden", slug="garden", description="A garden", cover_image="t.jpg")
        response = self.client.get("/ru/portfolio/garden/")
        self.assertContains(response, "Beautiful Garden")


@override_settings(ROOT_URLCONF="config.urls")
class PortfolioAdminTest(TestCase):
    def setUp(self):
        from django.contrib.auth.models import User

        self.admin = User.objects.create_superuser("admin", "admin@test.com", "password")
        self.client.login(username="admin", password="password")

    def test_project_admin_accessible(self):
        response = self.client.get("/ru/admin/portfolio/project/")
        self.assertEqual(response.status_code, 200)

    def test_category_admin_accessible(self):
        response = self.client.get("/ru/admin/portfolio/category/")
        self.assertEqual(response.status_code, 200)
