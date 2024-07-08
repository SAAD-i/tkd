from django.contrib import admin
from django.urls import path, include
from users import urls as users_urls
from subscription import urls as subscription_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include(users_urls)),
    path('subscription/', include(subscription_urls)),
]
