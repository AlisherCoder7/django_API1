from rest_framework import viewsets
from .models import FAQ,Feature,News
from .serializers import FeatureSerializer,NewsSerializer,FAQSerializer
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

@method_decorator(cache_page(60 * 15),name='dispatch')
class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


@method_decorator(cache_page(60 * 15),name='dispatch')
class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer


@method_decorator(cache_page(60 * 15),name='dispatch')
class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
