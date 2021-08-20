from django.urls import path

from subsrcibeapp.views import SubscriptionView, SubscriptionListView

app_name = 'subscribeapp'

urlpatterns = [
    path('subcribe/<int:project_pk>', SubscriptionView.as_view(), name='subscribe'),
    path('list/',SubscriptionListView.as_view(), name='list'),
]