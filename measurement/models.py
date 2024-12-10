from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(u'Название', max_length=50)
    description = models.TextField(u'Описание', null=True, blank=True)

    class Meta:
        unique_together = ['name', 'description']
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'
        db_table = 'sensors'

    def __str__(self):
        return self.name
    
class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField(u'Температура')
    created_at = models.DateTimeField(u'Время создания записи', auto_now_add=True)

    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'
        db_table = 'measurements'
