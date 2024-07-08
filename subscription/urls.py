from django.urls import path
from .views import SubscriptionPlan, SubscriptionView
urlpatterns = [
    path('add/',SubscriptionView.as_view(),name='add_subscription'),
    path('remove/',SubscriptionView.as_view(),name='remove_subscription')
]
