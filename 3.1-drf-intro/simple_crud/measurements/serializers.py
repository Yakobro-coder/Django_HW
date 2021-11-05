# TODO: опишите сериализаторы
from rest_framework import serializers
from .models import Project, Measurement


class MeasurementModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = "__all__"

    # id = serializers.IntegerField(read_only=True)
    # value = serializers.FloatField()
    # project = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # created_at = serializers.DateTimeField(
    #     auto_now_add=True
    # )
    # updated_at = serializers.DateTimeField(
    #     auto_now=True
    # )


class ProjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField()
    # latitude = serializers.FloatField()
    # longitude = serializers.FloatField()
    # created_at = serializers.DateTimeField(
    #     auto_now_add=True
    # )
    # updated_at = serializers.DateTimeField(
    #     auto_now=True
    # )
