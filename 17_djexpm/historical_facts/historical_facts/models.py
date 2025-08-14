from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    description = models.TextField(blank=True, verbose_name="Descripción")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.name

class HistoricalFact(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    date = models.DateField(verbose_name="Fecha")
    location = models.CharField(max_length=100, verbose_name="Lugar")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Categoría")
    image = models.ImageField(upload_to='historical_facts/', blank=True, null=True, verbose_name="Imagen")
    source = models.CharField(max_length=200, blank=True, verbose_name="Fuente")
    is_featured = models.BooleanField(default=False, verbose_name="Destacado")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Hecho Histórico"
        verbose_name_plural = "Hechos Históricos"
        ordering = ['-date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('fact_detail', kwargs={'pk': self.pk})
