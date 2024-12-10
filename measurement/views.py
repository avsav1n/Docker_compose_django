# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.forms.models import model_to_dict
from django.shortcuts import redirect
from rest_framework.generics import (CreateAPIView, ListAPIView,
                                     RetrieveAPIView, RetrieveUpdateAPIView)
from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.models import Measurement, Sensor
from measurement.serializers import (MeasurementSerializer,
                                     SensorDetailSerializer, SensorSerializer)


class SensorsView(APIView):
    def get(self, request):
        sensors = Sensor.objects.all()
        serializer = SensorSerializer(sensors, many=True,)
        return Response(serializer.data)

    def post(self, request):
        new_sensor = Sensor.objects.get_or_create(**request.data)
        serializer = SensorSerializer(new_sensor[0])
        return Response({**serializer.data,
                         'created': new_sensor[1],
                         'exist': not new_sensor[1]})


class DetailSensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def patch(self, request, pk):
        sensor = Sensor.objects.get(pk=pk)
        flag = False
        for attr, value in request.data.items():
            flag = flag or getattr(sensor, attr) != value
            setattr(sensor, attr, value)
        if flag:
            sensor.save()
        serializer = SensorSerializer(sensor)
        return Response({**serializer.data,
                         'updated': flag})


# class CreateSensorsView(CreateAPIView):
#     serializer_class = SensorSerializer


# class UpdateSensorView(RetrieveUpdateAPIView):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorSerializer


class MeasurementsView(CreateAPIView):
    def post(self, request):
        measurement_info = request.data.copy()
        measurement_info['sensor'] = Sensor.objects.get(pk=request.data['sensor'])
        measurement = Measurement.objects.create(**measurement_info)
        serializer = MeasurementSerializer(measurement)
        return Response(serializer.data)


# class CreateMeasurementsView(CreateAPIView):
#     serializer_class = MeasurementSerializer


def admin_redirect(request):
    return redirect('admin/')
