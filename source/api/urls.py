from django.urls import path

from api.views import AddFrendsView

app_name = 'api'

urlpatterns = [
    path('api/add_friends/', AddFrendsView.as_view(), name='add_friends'),
]