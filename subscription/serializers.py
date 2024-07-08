from rest_framework import serializers
from .models import Subscription, SubscriptionPlan
class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['user','plan','start_date','end_date','is_active']