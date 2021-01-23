from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from webapp.models import Message


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    template_name = 'message_detail.html'
    permission_required = 'employees.can_view_employee'