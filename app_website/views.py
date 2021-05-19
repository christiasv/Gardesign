from django.views.generic import TemplateView

from app_administracion.models.blogs import Blog
from app_administracion.models.comments import Comments
from app_administracion.models.detail_company import DetailCompany
from app_administracion.models.product import Category, Product, GalleryImgProduct
from app_administracion.models.service import Service, GalleryImgService
from app_website.models.html_carrusel import Slider
from app_website.models.html_we import HtmlWe, We
from django_configurations.models import Configurations


class BaseTemplate(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['url_whatsapp'] = Configurations.objects.get(key='url.whatsapp').clean_value
        except Configurations.DoesNotExist:
            context['url_whatsapp'] = ''

        try:
            context['url_instagram'] = Configurations.objects.get(key='url.instagram').clean_value
        except Configurations.DoesNotExist:
            context['url_instagram'] = ''

        try:
            context['url_facebook'] = Configurations.objects.get(key='url.facebook').clean_value
        except Configurations.DoesNotExist:
            context['url_facebook'] = ''
        return context


class HomeView(BaseTemplate):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = Slider.objects.filter(type=Slider.INICIO)
        context['blogs'] = Blog.objects.all().order_by('-created')[:10]
        context['categories'] = Category.objects.all()
        context['comments'] = Comments.objects.all().order_by('-created')[:10]
        context['productos'] = Product.objects.all().order_by('-created')[:10]
        return context


class AboutView(BaseTemplate):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['html_we'] = HtmlWe.objects.get(activate=True)
        context['we'] = We.objects.get(activate=True)
        context['comments'] = Comments.objects.all().order_by('-created')[:5]
        return context


class ShopView(BaseTemplate):
    template_name = 'shop.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id_category'] = self.kwargs['pk'] if 'pk' in self.kwargs else None
        context['search_inicial'] = self.request.GET['search_inicial'] if 'search_inicial' in self.request.GET else None
        context['categories'] = Category.objects.all()
        return context


class ShopDetailView(BaseTemplate):
    template_name = 'shopdetail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos'] = GalleryImgProduct.objects.filter(producto_id=self.kwargs['pk'])
        context['img_init'] = GalleryImgProduct.objects.filter(producto_id=self.kwargs['pk'])[0]
        context['ultimos_productos'] = Product.objects.exclude(id=self.kwargs['pk'])[:10]
        return context


class ServicesView(BaseTemplate):
    template_name = 'services.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        return context


class ServicesDetailView(BaseTemplate):
    template_name = 'servicesdetail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service'] = Service.objects.get(id=self.kwargs['pk'])
        context['gallery'] = GalleryImgService.objects.filter(service_id=self.kwargs['pk'])
        return context


class BlockDetailView(BaseTemplate):
    template_name = 'blogdetails.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog'] = Blog.objects.get(id=self.kwargs['pk'])
        context['ultimos_blogs'] = Blog.objects.exclude(id=self.kwargs['pk']).order_by('-created')[:8]
        return context


class ProjectsView(BaseTemplate):
    template_name = 'projects.html'


class BlogView(BaseTemplate):
    template_name = 'blog.html'


class BlogDetailsView(BaseTemplate):
    template_name = 'blogdetails.html'


class ContactView(BaseTemplate):
    template_name = 'contact.html'
    model = DetailCompany

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data_company = DetailCompany.objects.get(activate=True)
        context['detail_company'] = data_company
        return context


class FaqView(BaseTemplate):
    template_name = 'faq.html'
