from django.views.generic import TemplateView

from apps.portfolio.models import Project

from .models import AboutSection, HeroSection, ServiceItem


class HomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["heroes"] = HeroSection.objects.filter(is_active=True)
        ctx["services"] = ServiceItem.objects.all()
        ctx["about"] = AboutSection.objects.first()
        ctx["featured_projects"] = Project.objects.filter(is_published=True)[:5]
        return ctx
