from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from webapp.models import Message


class MessageInboxListView(LoginRequiredMixin, ListView):
    template_name = 'message_list_input.html'
    context_object_name = 'messages'
    paginate_by = 5
    paginate_orphans = 4

    def get_queryset(self):
        queryset = Message.objects.all().filter(recipient=self.request.user).order_by('-pk')
        return queryset

class MessageOutListView(LoginRequiredMixin, ListView):
    template_name = 'message_list.html'
    context_object_name = 'messages'
    paginate_by = 5
    paginate_orphans = 4

    def get_queryset(self):
        queryset = Message.objects.all().filter(author=self.request.user).order_by('-pk')
        return queryset