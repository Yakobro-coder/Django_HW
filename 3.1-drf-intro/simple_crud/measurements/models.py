from django.db import models


class DateTimeInfo(models.Model):
    """Мета Класс с наследуемыми полями."""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Project(DateTimeInfo):
    """Объект на котором проводят измерения."""

    name = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()


class Measurement(DateTimeInfo):
    """Измерение температуры на объекте."""

    value = models.FloatField()
    nullable_image = models.ImageField(blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
