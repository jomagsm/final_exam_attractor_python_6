from django.urls import path

from webapp.views.message_create_view import MessageCreateView

app_name = 'webapp'

urlpatterns = [
    path('message_add/<int:pk>/', MessageCreateView.as_view(), name='message_add'),
]