from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.mixins import ListModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from app_administracion.api.serializers import ServiceSerializer, ProductSerializer, ContactoSerializer, BlogSerializer
from app_administracion.models.blogs import Blog
from app_administracion.models.contacto import Contacto
from app_administracion.models.product import Product
from app_administracion.models.service import Service

DEFAULT_PAGE = 1
DEFAULT_PAGE_SIZE = 10


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'total': self.page.paginator.count,
            'page': int(self.request.GET.get('page', DEFAULT_PAGE)),  # can not set default = self.page
            'page_size': int(self.request.GET.get('page_size', self.page_size)),
            'results': data
        })


class ListServiceViewSet(ListModelMixin, GenericViewSet):
    queryset = None
    serializer_class = None


class ListServiceApiViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ListProductApiViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        qs = super().get_queryset()
        params = dict(self.request.query_params)
        if 'category' in params:
            qs = qs.filter(category_id=int(params['category'][0]))
        if 'searchp' in params:
            qs = qs.filter(name__contains=params['searchp'][0])
        return qs


class ListBlogApiViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']

    def filter_queryset(self, queryset):
        if len(self.request.query_params) == 0:
            return queryset
        return queryset.filter(title__contains=dict(self.request.query_params)['title'][0])


class DetailProductApiViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CreateContactoApiViewSet(ModelViewSet):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer
