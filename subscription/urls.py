from django.urls import path
from .views import SubscriptionPlan, SubscriptionView
urlpatterns = [
    path('get/<str:id>', SubscriptionView.as_view(), name='get_subscription_view'),
    path('post/', SubscriptionView.as_view(), name='post_subscription_view'),
    path('delete/<str:id>', SubscriptionView.as_view(), name='delete_subscription_view'),
    path('update/<str:id>', SubscriptionView.as_view(), name='update_subscription_view'),
    path('getall/', SubscriptionView.as_view(), name='get_all_subscription_view'),
    path('plan/get/<str:id>', SubscriptionView.as_view(), name='get_plan_view'),
    path('plan/post/', SubscriptionView.as_view(), name='post_plan_view'),
    path('plan/delete/<str:id>', SubscriptionView.as_view(), name='delete_plan_view'),
    path('plan/update/<str:id>', SubscriptionView.as_view(), name='update_plan_view'),
    path('plans/getall/', SubscriptionView.as_view(), name='get_all_plans_view'),
]
