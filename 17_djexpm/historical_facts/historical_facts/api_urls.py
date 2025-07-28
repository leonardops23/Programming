from django.urls import path
from . import api_views

urlpatterns = [
    # Categorías
    path('categories/', api_views.CategoryListCreateView.as_view(), name='api_category_list'),
    path('categories/<int:pk>/', api_views.CategoryDetailView.as_view(), name='api_category_detail'),
    path('categories/<int:category_id>/facts/', api_views.CategoryFactsView.as_view(), name='api_category_facts'),
    
    # Hechos históricos
    path('facts/', api_views.HistoricalFactListView.as_view(), name='api_fact_list'),
    path('facts/create/', api_views.HistoricalFactCreateView.as_view(), name='api_fact_create'),
    path('facts/<int:pk>/', api_views.HistoricalFactDetailView.as_view(), name='api_fact_detail'),
    path('facts/<int:pk>/update/', api_views.HistoricalFactUpdateView.as_view(), name='api_fact_update'),
    path('facts/<int:pk>/delete/', api_views.HistoricalFactDeleteView.as_view(), name='api_fact_delete'),
    
    # Endpoints especiales
    path('facts/featured/', api_views.FeaturedFactsView.as_view(), name='api_featured_facts'),
    path('search/', api_views.search_facts, name='api_search_facts'),
    path('stats/', api_views.api_stats, name='api_stats'),
]
from django.core.management.base import BaseCommand
from historical_facts.models import Category, HistoricalFact
from datetime import date

class Command(BaseCommand):
    help = 'Carga datos de ejemplo'

    def handle(self, *args, **options):
        # Crear categorías
        categories_data = [
            {'name': 'Guerras Mundiales', 'description': 'Eventos relacionados con las grandes guerras del siglo XX'},
            {'name': 'Descubrimientos', 'description': 'Grandes descubrimientos científicos y geográficos'},
            {'name': 'Revoluciones', 'description': 'Movimientos revolucionarios que cambiaron la historia'},
            {'name': 'América Latina', 'description': 'Eventos importantes en la historia latinoamericana'},
        ]

        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={'description': cat_data['description']}
            )
            if created:
                self.stdout.write(f'Categoría creada: {category.name}')

        # Crear hechos históricos
        facts_data = [
            {
                'title': 'Independencia del Ecuador',
                'description': 'El 24 de mayo de 1822, tras la Batalla de Pichincha liderada por Antonio José de Sucre, Ecuador logró su independencia del dominio español. Este evento marcó el fin del período colonial y el inicio de la vida republicana del país.',
                'date': date(1822, 5, 24),
                'location': 'Quito, Ecuador',
                'category': 'América Latina',
                'is_featured': True,
            },
            {
                'title': 'Descubrimiento de América',
                'description': 'El 12 de octubre de 1492, Cristóbal Colón llegó a América, específicamente a la isla de Guanahani en las Bahamas. Este evento cambió para siempre la historia mundial, conectando dos continentes y dando inicio a la época colonial.',
                'date': date(1492, 10, 12),
                'location': 'Bahamas',
                'category': 'Descubrimientos',
                'is_featured': True,
            },
            {
                'title': 'Inicio de la Primera Guerra Mundial',
                'description': 'El 28 de julio de 1914 comenzó la Primera Guerra Mundial tras el asesinato del archiduque Francisco Fernando de Austria. Este conflicto involucró a las principales potencias mundiales y cambió el mapa político de Europa.',
                'date': date(1914, 7, 28),
                'location': 'Europa',
                'category': 'Guerras Mundiales',
                'is_featured': True,
            },
            {
                'title': 'Revolución Francesa',
                'description': 'La Revolución Francesa comenzó en 1789 con la toma de la Bastilla el 14 de julio. Este movimiento revolucionario terminó con el Antiguo Régimen y estableció los principios de libertad, igualdad y fraternidad.',
                'date': date(1789, 7, 14),
                'location': 'París, Francia',
                'category': 'Revoluciones',
                'is_featured': False,
            },
            {
                'title': 'Llegada del hombre a la Luna',
                'description': 'El 20 de julio de 1969, Neil Armstrong y Buzz Aldrin se convirtieron en los primeros seres humanos en pisar la superficie lunar durante la misión Apollo 11 de la NASA.',
                'date': date(1969, 7, 20),
                'location': 'Luna',
                'category': 'Descubrimientos',
                'is_featured': True,
            },
        ]

        for fact_data in facts_data:
            category = Category.objects.get(name=fact_data['category'])
            fact_data['category'] = category
            
            fact, created = HistoricalFact.objects.get_or_create(
                title=fact_data['title'],
                defaults=fact_data
            )
            if created:
                self.stdout.write(f'Hecho histórico creado: {fact.title}')

        self.stdout.write(self.style.SUCCESS('Datos de ejemplo cargados exitosamente'))
