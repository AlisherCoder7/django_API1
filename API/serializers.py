from rest_framework import serializers
from .models import FAQ,Feature,News


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ['id','name','description']



class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id','question','answer']


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id','title','content','created_ad']

