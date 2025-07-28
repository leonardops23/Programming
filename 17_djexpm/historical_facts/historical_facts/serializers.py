from rest_framework import serializers
from .models import Category, HistoricalFact

class CategorySerializer(serializers.ModelSerializer):
    facts_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_at', 'facts_count']
        read_only_fields = ['created_at']
    
    def get_facts_count(self, obj):
        return obj.historicalfact_set.count()

class HistoricalFactListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = HistoricalFact
        fields = [
            'id', 'title', 'description', 'date', 'location',
            'category', 'category_id', 'image', 'source',
            'is_featured', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']

class HistoricalFactDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    related_facts = serializers.SerializerMethodField()
    
    class Meta:
        model = HistoricalFact
        fields = [
            'id', 'title', 'description', 'date', 'location',
            'category', 'category_id', 'image', 'source',
            'is_featured', 'created_at', 'updated_at', 'related_facts'
        ]
        read_only_fields = ['created_at', 'updated_at']
    
    def get_related_facts(self, obj):
        related = HistoricalFact.objects.filter(
            category=obj.category
        ).exclude(id=obj.id)[:3]
        return HistoricalFactListSerializer(related, many=True, context=self.context).data

class HistoricalFactCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalFact
        fields = [
            'title', 'description', 'date', 'location',
            'category', 'image', 'source', 'is_featured'
        ]
