from rest_framework.serializers import Serializer
from .models import Page



class PageSerializer(Serializer.ModelSerializer):
    class Meta:
        model = Page
        fields = ['title', 'content', 'slug', 'tools']