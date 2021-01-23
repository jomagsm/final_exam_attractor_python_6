from django.urls import path

from api.views import AddFrendsView, DeleteFrendsView

app_name = 'api'

urlpatterns = [
    path('api/add_friends/', AddFrendsView.as_view(), name='add_friends'),
    path('api/del_friends/<int:pk>/', DeleteFrendsView.as_view(), name='del_friends'),
]