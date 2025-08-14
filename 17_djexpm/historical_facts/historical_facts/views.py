from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import HistoricalFact, Category

class HomeView(ListView):
    model = HistoricalFact
    template_name = 'historical_facts/home.html'
    context_object_name = 'facts'
    paginate_by = 6

    def get_queryset(self):
        return HistoricalFact.objects.filter(is_featured=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['recent_facts'] = HistoricalFact.objects.all()[:5]
        return context

class FactListView(ListView):
    model = HistoricalFact
    template_name = 'historical_facts/fact_list.html'
    context_object_name = 'facts'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class FactDetailView(DetailView):
    model = HistoricalFact
    template_name = 'historical_facts/fact_detail.html'
    context_object_name = 'fact'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_facts'] = HistoricalFact.objects.filter(
            category=self.object.category
        ).exclude(pk=self.object.pk)[:3]
        return context

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'historical_facts/category_detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['facts'] = HistoricalFact.objects.filter(category=self.object)
        return context

class SearchView(ListView):
    model = HistoricalFact
    template_name = 'historical_facts/search_results.html'
    context_object_name = 'facts'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return HistoricalFact.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(location__icontains=query)
            )
        return HistoricalFact.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context