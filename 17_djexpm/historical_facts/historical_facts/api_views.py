from rest_framework import generics, filters, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from .models import Category, HistoricalFact
from .serializers import (
    CategorySerializer, 
    HistoricalFactListSerializer,
    HistoricalFactDetailSerializer,
    HistoricalFactCreateUpdateSerializer
)

class CategoryListCreateView(generics.ListCreateAPIView):
    """
    Lista todas las categorías o crea una nueva.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Obtiene, actualiza o elimina una categoría específica.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class HistoricalFactListView(generics.ListAPIView):
    """
    Lista todos los hechos históricos con filtros y búsqueda.
    """
    queryset = HistoricalFact.objects.all()
    serializer_class = HistoricalFactListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'is_featured', 'date']
    search_fields = ['title', 'description', 'location']
    ordering_fields = ['date', 'created_at', 'title']
    ordering = ['-date']

class HistoricalFactCreateView(generics.CreateAPIView):
    """
    Crea un nuevo hecho histórico.
    """
    queryset = HistoricalFact.objects.all()
    serializer_class = HistoricalFactCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

class HistoricalFactDetailView(generics.RetrieveAPIView):
    """
    Obtiene los detalles de un hecho histórico específico.
    """
    queryset = HistoricalFact.objects.all()
    serializer_class = HistoricalFactDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class HistoricalFactUpdateView(generics.UpdateAPIView):
    """
    Actualiza un hecho histórico específico.
    """
    queryset = HistoricalFact.objects.all()
    serializer_class = HistoricalFactCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

class HistoricalFactDeleteView(generics.DestroyAPIView):
    """
    Elimina un hecho histórico específico.
    """
    queryset = HistoricalFact.objects.all()
    permission_classes = [IsAuthenticated]

class FeaturedFactsView(generics.ListAPIView):
    """
    Lista solo los hechos históricos destacados.
    """
    queryset = HistoricalFact.objects.filter(is_featured=True)
    serializer_class = HistoricalFactListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CategoryFactsView(generics.ListAPIView):
    """
    Lista los hechos históricos de una categoría específica.
    """
    serializer_class = HistoricalFactListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['date', 'created_at', 'title']
    ordering = ['-date']

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return HistoricalFact.objects.filter(category_id=category_id)

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def search_facts(request):
    """
    Búsqueda avanzada de hechos históricos.
    """
    query = request.GET.get('q', '')
    category_id = request.GET.get('category', None)
    is_featured = request.GET.get('featured', None)
    
    facts = HistoricalFact.objects.all()
    
    if query:
        facts = facts.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(location__icontains=query)
        )
    
    if category_id:
        facts = facts.filter(category_id=category_id)
    
    if is_featured is not None:
        facts = facts.filter(is_featured=is_featured.lower() == 'true')
    
    facts = facts.order_by('-date')
    
    serializer = HistoricalFactListSerializer(facts, many=True)
    
    return Response({
        'count': facts.count(),
        'results': serializer.data
    })

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def api_stats(request):
    """
    Estadísticas generales de la API.
    """
    total_facts = HistoricalFact.objects.count()
    featured_facts = HistoricalFact.objects.filter(is_featured=True).count()
    total_categories = Category.objects.count()
    
    return Response({
        'total_facts': total_facts,
        'featured_facts': featured_facts,
        'total_categories': total_categories,
    })
