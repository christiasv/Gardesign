from django.contrib import admin
from django.contrib.admin import TabularInline

from app_administracion.models.blogs import Blog
from app_administracion.models.comments import Comments
from app_administracion.models.contacto import Contacto
from app_administracion.models.detail_company import DetailCompany
from app_administracion.models.product import Product, Category, GalleryImgProduct
from app_administracion.models.service import Service, GalleryImgService


@admin.register(Category)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('name', 'cover_image')


class GalleryImgProductInline(TabularInline):
    model = GalleryImgProduct


@admin.register(Product)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'cover_image', 'more_info')
    inlines = [GalleryImgProductInline]


class GalleryImgServiceInline(TabularInline):
    model = GalleryImgService


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'cover_image', 'more_info')
    inlines = [GalleryImgServiceInline]


@admin.register(DetailCompany)
class DetailCompanyAdmin(admin.ModelAdmin):
    list_display = ['direction', 'activate']
    readonly_fields = ['activate']


@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'descripcion_corta', 'image')


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'comments')
