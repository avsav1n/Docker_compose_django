from django.urls import path

from measurement.views import SensorsView, MeasurementsView, DetailSensorView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorsView.as_view()),
    path('sensors/<int:pk>/', DetailSensorView.as_view()),
    path('measurements/', MeasurementsView.as_view()),
]
