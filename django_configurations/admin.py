from django.contrib import admin

from django_configurations.models import Configurations


@admin.register(Configurations)
class ExecutionAdmin(admin.ModelAdmin):
    list_display = ('key', 'obfuscated_value')

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ['clean_value']
        else:
            return []