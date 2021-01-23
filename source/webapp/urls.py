from django.urls import path

from webapp.views.message_create_view import MessageCreateView
from webapp.views.message_detail import MessageDetailView
from webapp.views.message_list_view import MessageInboxListView, MessageOutListView

app_name = 'webapp'

urlpatterns = [
    path('message_add/<int:pk>/', MessageCreateView.as_view(), name='message_add'),
    path('messageinbox/', MessageInboxListView.as_view(), name='message_inbox'),
    path('messageout/', MessageOutListView.as_view(),name='message_out'),
    path('messagedetail/<int:pk>', MessageDetailView.as_view(),name='message_detail'),
]