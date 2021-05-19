from django.contrib import admin

from app_website.models.html_carrusel import Slider
from app_website.models.html_we import HtmlWe, We


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo', 'type', 'more_info', 'active')


@admin.register(HtmlWe)
class HtmlWeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'cover_image', 'activate')
    readonly_fields = ['activate']


@admin.register(We)
class WeAdmin(admin.ModelAdmin):
    list_display = (
        'our_mission_title', 'our_mission_description',
        'our_vision_title', 'our_vision_description',
        'our_values_title', 'our_values_description',
        'activate')
    readonly_fields = ['activate']
    fieldsets = [
        ('Mision', {'fields': ['our_mission_title', 'our_mission_img', 'our_mission_description']}),
        ('Vision', {'fields': ['our_vision_title', 'our_vision_img', 'our_vision_description']}),
        ('Valores', {'fields': ['our_values_title', 'our_values_img', 'our_values_description']}),
        (None, {'fields': ['activate']}),
    ]
