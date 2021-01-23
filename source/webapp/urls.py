from django.urls import path

from webapp.views.message_create_view import MessageCreateView
from webapp.views.message_list_view import MessageInboxListView, MessageOutListView

app_name = 'webapp'

urlpatterns = [
    path('message_add/<int:pk>/', MessageCreateView.as_view(), name='message_add'),
    path('messageinbox/', MessageInboxListView.as_view(), name='message_inbox'),
    path('messageout/', MessageOutListView.as_view(),name='message_out'),
]