from django.urls import path, include

urlpatterns = [
    # ...
    path('prices/', include('prices.urls')),
    # ...
] 