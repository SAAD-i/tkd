from rest_framework.response import Response
from rest_framework.decorators import APIView
from django.contrib.auth import get_user_model
from .serializers import SubscriptionSerializer
from .models import SubscriptionPlan
from django.shortcuts import get_object_or_404
from django.conf import settings
from .models import Subscription

User = get_user_model()
# Create your views here.
class SubscriptionPlanView(APIView):
    def post(self, request):
        message = 'Subscription Plan.'
        return Response(message)


class SubscriptionView(APIView):
    # permission_classes = []
    def post(self, request):
        subscription = Subscription()
        user_id = request.data['user']
        user = get_object_or_404(User, id=user_id)
        plan_id = request.data['plan']
        plan = get_object_or_404(SubscriptionPlan, id=plan_id)
        end_date = request.data['end_date']
        subscription.user = user
        subscription.plan = plan
        subscription.end_date = end_date
        subscription.save()
        user.is_pro = True
        user.save()
        return Response('Hello')
                        
        