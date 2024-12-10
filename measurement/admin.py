from django.contrib import admin

from measurement.models import Sensor, Measurement


# Register your models here.
class MeasurementInline(admin.TabularInline):
    extra = 0
    model = Measurement


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description_column']
    inlines = [MeasurementInline]

    @admin.display(description='Описание', ordering='description')
    def description_column(self, obj):
        max_len = 20
        return obj.description[:max_len] + ('...' if len(obj.description) > max_len else '')


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ['temperature', 'created_at']
    list_filter = ['sensor']