from rest_framework.serializers import Serializer
from .models import AdminSetting


class SettingSerializer(Serializer.ModelSerializer):
    class Meta:
        model = AdminSetting
        fields = '__all__'